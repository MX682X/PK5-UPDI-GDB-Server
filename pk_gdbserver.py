#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pyOCD debugger
# Copyright (c) 2006-2020 Arm Limited
# Copyright (c) 2021-2022 Chris Reed
# Copyright (c) 2022 Clay McClure
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# The above License Notice is due to the fact that I just copy pasted a lot
# from the pyOCD Debugger Project to avoid doing the same work again.
# However, the code is still modified, on one hand, because of the
# reduced complexity and variety of the AVR core, and on the other to
# understand what happens



import logging
import array
import socket
import pyocd
import threading
import queue
from pk_debugger_iface import pk_debugger
from time import sleep
from typing import (Dict, List, Optional, Tuple)


LOG = logging.getLogger(__name__)

## Tuple of int values of characters that must be escaped.
_GDB_ESCAPED_CHARS = tuple(b'#$}*')

def escape(data):
    """@brief Escape binary data to be sent to Gdb.

    @param data Bytes-like object containing raw binary.
    @return Bytes object with the characters in '#$}*' escaped as required by Gdb.
    """
    result = []
    for c in data:
        if c in _GDB_ESCAPED_CHARS:
            # Escape by prefixing with '}' and xor'ing the char with 0x20.
            result += [0x7d, c ^ 0x20]
        else:
            result.append(c)
    return bytes(result)

def unescape(data: bytes) -> List[int]:
    """@brief De-escapes binary data from Gdb.

    @param data Bytes-like object with possibly escaped values.
    @return List of integers in the range 0-255, with all escaped bytes de-escaped.
    """
    data_idx = 0

    # unpack the data into binary array
    result = list(data)

    # check for escaped characters
    while data_idx < len(result):
        if result[data_idx] == 0x7d:
            result.pop(data_idx)
            result[data_idx] = result[data_idx] ^ 0x20
        data_idx += 1

    return result




class gdb_server(threading.Thread):
    def __init__(self, port:int, debugger:pk_debugger):
        super().__init__()
        self._event_queue = queue.Queue()
        self.shutdown_event = threading.Event()
        self.detach_event = threading.Event()
        self.lock = threading.Lock()
        self.debugger:pk_debugger = debugger
        self.packet_io = gdbserver_socket_io_thread(port, self._event_queue)
        self.target = None
        self.session = None
        self.packet_size = 2048
        self.persistence = False    # Keep connection open upon program finish
        
        self._programming_state = 0

        self.first_run_after_reset_or_flash = True
        self.COMMANDS = {
        #       CMD    HANDLER                   START    DESCRIPTION
                b'!' : (self.extended_remote,    0   ), # Enable extended remote mode.
                b'?' : (self.stop_reason_query,  0   ), # Stop reason query.
                b'c' : (self.resume,             1   ), # Continue (at addr)
                b'C' : (self.resume,             1   ), # Continue with signal.
                b'D' : (self.detach,             1   ), # Detach.
                b'g' : (self.get_registers,      0   ), # Read general registers.
                b'G' : (self.set_registers,      2   ), # Write general registers.
                b'H' : (self.set_thread,         2   ), # Set thread for subsequent operations.
                b'k' : (self.kill,               0   ), # Kill.
                b'm' : (self.get_memory,         2   ), # Read memory.
#                b'M' : (self.write_memory_hex,   2   ), # Write memory (hex).
                b'p' : (self.read_register,      2   ), # Read register.
                b'P' : (self.write_register,     2   ), # Write register.
                b'q' : (self.handle_query,       2   ), # General query.
                b'Q' : (self.handle_general_set, 2   ), # General set.
                b'R' : (self.restart,            1   ), # Extended remote restart command.
                b's' : (self.step,               1   ), # Single step.
                b'S' : (self.step,               1   ), # Step with signal.
                b'T' : (self.is_thread_alive,    1   ), # Thread liveness query.
                b'v' : (self.v_command,          2   ), # v command.
                b'X' : (self.write_memory,       2   ), # Write memory (binary).
                b'z' : (self.breakpoint,         1   ), # remove breakpoint/watchpoint.
                b'Z' : (self.breakpoint,         1   ), # Insert breakpoint/watchpoint.
            }

        self.setDaemon(True)
        self.start()
        print('GDB server started on port {0}'.format(port))
    #EOF

    def stop(self, wait=True):
        if self.is_alive():
            self.shutdown_event.set()
            if wait:
                self.join()
                pass
    
    def run(self):
        while not self.shutdown_event.is_set():
            if self.shutdown_event.is_set():
                break

                # Make sure the target is halted. Otherwise gdb gets easily confused.
                #self.target.halt()
                
            self._run_connection()
            
            sleep(0.1)
        print("Stopping server thread")
        self.stop()
        #self._cleanup()

    def _run_connection(self):
        assert self.packet_io

        self.detach_event.clear()

        while not (self.detach_event.is_set() or self.shutdown_event.is_set()):
            if self.packet_io.interrupt_event.is_set():
                print("GDB Received Interrupt, Got ctrl-c, halting")
                self.debugger.halt_Target()
                self.is_target_running = False
                self.send_stop_notification()
                self.packet_io.interrupt_event.clear()

            try:
                event = self._event_queue.get(False)
                if event == "disconnect":
                    self.debugger.detach_target()
                    self.detach_event.set()
                    break
            except queue.Empty:
                pass

            # read command
            packet = self.packet_io.receive(block=True)

            if self.shutdown_event.is_set():
                break

            if packet is None:
                sleep(0.1)
                continue

            if packet is not None and len(packet) != 0:
                # decode and prepare resp
                resp = self.handle_message(packet)

                if resp is not None:
                    # send resp
                    self.packet_io.send(resp)

        print("gdbserver exiting connection loop")

        # Clean up the connection.
        self.packet_io.stop()

        # If persisting is not enabled, we exit on detach. Otherwise prepare for a new connection.
        #if self.persist:
            #print("preparing for next connection")
            #self._cleanup_for_next_connection()
        #else:
         #   self.shutdown_event.set()
    #EOF


    def create_rsp_packet(self, data):
        resp = b'$' + data + b'#' + checksum(data)
        return resp
    #EOF


    def handle_query_xml(self, query: bytes, annex: bytes, offset: int, size: int) -> bytes:
        print('GDB query {0}: annex: {1}, offset: {2}, size: {3}'.format(query, annex, offset, size))

        # For each query object, we check the annex and return E00 for invalid values. Only 'features'
        # has a non-empty annex.
        if query == b'memory-map':
            if annex != b'':
                return self.create_rsp_packet(b"E00")
            xml = self.debugger.get_memory_map_xml()
        elif query == b'features':
            if annex == b'target.xml':
                xml = self.debugger.get_target_xml()
            else:
                return self.create_rsp_packet(b"E00")
        elif query == b'threads':
            if annex != b'':
                return self.create_rsp_packet(b"E00")
            xml = self.debugger.get_threads_xml()
        else:
            # Unrecognised query object, so return empty packet.
            print("Unsupported XML query ({0}), annex ({1})".format(query, annex))
            return self.create_rsp_packet(b"")

        size_xml = len(xml)

        prefix = b'm'

        if offset > size_xml:
            LOG.error('GDB requested xml offset > size for {0}!'.format(query))
            return self.create_rsp_packet(b"E16") # EINVAL

        if size > (self.packet_size - 4):
            size = self.packet_size - 4

        nbBytesAvailable = size_xml - offset

        if size > nbBytesAvailable:
            prefix = b'l'
            size = nbBytesAvailable

        resp = prefix + escape(xml[offset:offset + size])

        return resp
    #EOF

    def handle_message(self, msg):
        if msg[0:1] != b'$':
            print("Invalid Start of Packet received: {0}".format(msg[0:1]))
            return self.create_rsp_packet(b"E01")

        try:
            handler, msgStart = self.COMMANDS[msg[1:2]]
        except (KeyError, IndexError):
            print("Received: {0}".format(msg))
            #print("Unknown RSP command ({0})".format(msg[1:2]))
            return self.create_rsp_packet(b"")

        with self.lock:
            if msgStart == 0:
                reply = handler()
            else:
                reply = handler(msg[msgStart:])

        return reply

    #EOF

    def extended_remote(self):
        print("GDB Received: Enable extended remote")
        self._is_extended_remote = True
        return self.create_rsp_packet(b"OK")
        #EOF
    

    def detach(self, data):
        print("Detaching Target")
        # In extended-remote mode, detach should detach from the program but not close the connection. gdb assumes
        # the server connection is still valid. Detaching from the program doesn't really make sense for embedded
        # targets, so just ignore the detach.
        self.debugger.detach_target()
        if not self._is_extended_remote:
            self.detach_event.set()
        return self.create_rsp_packet(b"OK")
    

    def kill(self):
        print("GDB kill")
        self.debugger.detach_target() # Disable Power to Target
        # No packet is returned from the 'k' command.


    def restart(self, data):
        self.debugger.reset_Target()


    def stop_reason_query(self):
        # In non-stop mode, if no threads are stopped we need to reply with OK.
        print("GDB Received: Query Stop Reason")
        #if self.non_stop and self.is_target_running:
        #    return self.create_rsp_packet(b"OK")

        return self.create_rsp_packet(self.get_t_response())
        #EOF


    def handle_query(self, msg:bytes):
        query = msg.split(b':')
        print('GDB received query: {0}'.format(query))

        if query is None:
            print('GDB received malformed query packet')
            return None

        if query[0] == b'Supported':
            # Save features sent by gdb.
            self.gdb_features = query[1].split(b';')

            # Build our list of features.
            # Wrote code to return the cpu regs but avr-gdb already has a list.
            # And it does not allow a custom list. That's a couple hours wasted
            # Can't get memory map to woark either.
            # b'qXfer:memory-map:read+'
            features = [b'qXfer:features:read+', b'QStartNoAckMode+', b'qXfer:threads:read+', b'qXfer:memory-map:read+']
            features.append(b'PacketSize=' + (hex(self.packet_size).encode())[2:])
            resp = b';'.join(features)
            return self.create_rsp_packet(resp)

        elif query[0] == b'Xfer':
            # qXfer:<object>:read:<annex>:<offset>,<length>
            if query[2] == b'read':
                data = query[4].split(b',')
                resp = self.handle_query_xml(query[1], query[3], int(data[0], 16), int(data[1].split(b'#')[0], 16))
                return self.create_rsp_packet(resp)
            else:
                LOG.debug("Unsupported qXfer request: %s:%s:%s:%s", query[1], query[2], query[3], query[4])
                # Must return an empty packet for an unrecognized qXfer.
                return self.create_rsp_packet(b"")

        elif query[0].startswith(b'C'):
            return self.create_rsp_packet(b"QC1")

        elif query[0].find(b'Attached') != -1:
            return self.create_rsp_packet(b"1")

        elif query[0].find(b'TStatus') != -1:
            return self.create_rsp_packet(b"")

        elif query[0].find(b'Tf') != -1:
            return self.create_rsp_packet(b"")

        elif b'Offsets' in query[0]:
            resp = b"Text=0;Data=0;Bss=0" # Data Offset: 0x80 0000
            return self.create_rsp_packet(resp)

        elif b'Symbol' in query[0]:
            return self.create_rsp_packet(b"OK")

        elif query[0].startswith(b'Rcmd,'):
            cmd_raw = query[0][5:].split(b'#')[0]
            cmd = bytes.fromhex(cmd_raw.decode("ascii"))

            return self.handle_remote_command(cmd)

        else:
            return self.create_rsp_packet(b"")
        #EOF


    def set_thread(self, data:bytes):
        op = data[0:1]
        thread_id = int(data[1:-3], 16)
        print("GDB Received: Set Thread: {0}".format(thread_id))

        if thread_id == 0:
            print("Attatching PK to target")
            self.debugger.attach_target()

        return self.create_rsp_packet(b'OK')


    def is_thread_alive(self, data):
        threadId = int(data[1:-3], 16)
        print("GDB is inquiring state of Thread {0}".format(threadId))

        if (threadId == 1):
            return self.create_rsp_packet(b'OK')
        else:
            #self.validate_debug_context()
            return self.create_rsp_packet(b'E00')
        #EOF


    def send_stop_notification(self, forceSignal=0):
        data = self.get_t_response(force_signal=forceSignal)
        #data =  b"thread:1;" + b"S18"
        packet = b'%Stop:' + data + b'#' + checksum(data)
        print("Sending Stop Notification")
        self.packet_io.send(packet)
    

    def get_t_response(self, force_signal=0):
        """@brief Returns a GDB T response string.
        See https://sourceware.org/gdb/current/onlinedocs/gdb.html/Tracepoint-Packets.html#Tracepoint-Packets
        This includes:
        - The signal encountered.
        - The current value of the important registers (SREG, SP, PC).
        """
        response = ""
        if force_signal != 0:
            response += ("T" + self.debugger.conv_byte_to_hex(force_signal))
        else:
            response += ("T" + self.debugger.conv_byte_to_hex(0x11)) # Default to SIGSTOP

        cpu_regs = self.debugger.get_SP_SREG()
        cpu_pc = self.debugger.get_PC()
        # SREG
        response += (self.debugger.conv_byte_to_hex(32) + ":")
        response += (self.debugger.conv_byte_to_hex(cpu_regs[2]) + ";")
        # SP
        response += (self.debugger.conv_byte_to_hex(33) + ":")
        response +=  self.debugger.conv_byte_to_hex(cpu_regs[0])
        response +=  self.debugger.conv_byte_to_hex(cpu_regs[1])
        response += ";"
        # PC
        response += (self.debugger.conv_byte_to_hex(34) + ":")
        response += self.debugger.conv_byte_to_hex(cpu_pc[0])
        response += self.debugger.conv_byte_to_hex(cpu_pc[1])
        response += self.debugger.conv_byte_to_hex(cpu_pc[2])
        response += self.debugger.conv_byte_to_hex(cpu_pc[3])
        response += ";"
        response += "thread:01;"

        return response.encode("ascii")


    def v_command(self, data:bytes):
        cmd = data.split(b'#')[0]

        # Flash command.
        if cmd.startswith(b'Flash'):
            return self.flash_op(cmd)

        # v_cont capabilities query.
        elif b'Cont?' == cmd:
            print('GDB received v-Command: {0}'.format(cmd))
            return self.create_rsp_packet(b"vCont;c;C;s;S;r;t")

        # v_cont, thread action command.
        elif cmd.startswith(b'Cont'):
            print('GDB received v-Command: {0}'.format(cmd))
            return self.v_cont(cmd)

        # vStopped, part of thread stop state notification sequence.
        elif b'Stopped' in cmd:
            # Because we only support one thread for now, we can just reply OK to vStopped.
            print('GDB received v-Command: {0}'.format(cmd))
            return self.create_rsp_packet(b"OK")

        return self.create_rsp_packet(b"")
        #EOF


    def v_cont(self, cmd):
        ops = cmd.split(b';')[1:] # split and remove 'Cont' from list
        if not ops:
            return self.create_rsp_packet(b"OK")
        thread_actions = None
        default_action = None
        currentThread = 1

        for op in ops:
            args = op.split(b':')
            action = args[0][0:1]
            if action in (b"c", b"C"):
                print("GDB Resuming")
                return self.resume(None)
            elif action in (b"s", b"S"):
                #print("GDB Step")
                return self.step(None)
            elif action in (b"t"):
                print("GDB Stop")
                return self.create_rsp_packet(b"")
                #self.packet_io.send(self.create_rsp_packet(b"OK"))
                #self.send_stop_notification()
            elif action in (b"r"):
                signal = args[0][1:]
                start, end = signal.split(b',')
                start = int(start, 16)
                end = int(end, 16)
                return self.step(None, start, end)
        #EOF


    def flash_op(self, data):
        ops = data.split(b':')
        print("GDB Flash Command")
        
        if ops[0] == b'FlashErase':
            param = ops[1]
            start, length = param.split(b',')
            #start = int(start, 16)
            #length = int(length, 16)
            start = self.decode_hex_string(start)
            length = self.decode_hex_string(length)
            print("GDB Flash Erase: Start:0x{0:04X}, Len:0x{1:04X}".format(start, length))
            # doing only chip erase for now
            if (start == 0 and length >= 512):
                if (self.debugger.erase_target_flash()):
                    return self.create_rsp_packet(b"OK")
            return self.create_rsp_packet(b"E01")

        elif ops[0] == b'FlashWrite':
            start = ops[1]
            start = self.decode_hex_string(start)
            
            # search for second ':' (beginning of data encoded in the message)
            second_colon = 0
            idx_begin = 0
            while second_colon != 2:
                if data[idx_begin:idx_begin+1] == b':':
                    second_colon += 1
                idx_begin += 1
    
            payload = unescape(data[idx_begin:])
            print("GDB Flash Write: Start:0x{0:04X}, Len:0x{1:04X}".format(start, len(payload)))
            # Add data to flash loader
            self.debugger.prepare_target_flash(start, payload)

            return self.create_rsp_packet(b"OK")

        # we need to flash everything
        elif b'FlashDone' in ops[0] :
            print("GDB Flash Done command, Downloading to Target")
            self.debugger.finalize_download()
            return self.create_rsp_packet(b"OK")

        return None

    def handle_general_set(self, msg:bytes):
        feature = msg.split(b'#')[0]
        print("GDB general set: {0}".format(feature))

        if feature == b'StartNoAckMode':
            # Disable acks after the reply and ack.
            self.packet_io.set_send_acks(False)
            return self.create_rsp_packet(b"OK")

        #elif feature.startswith(b'NonStop'):
        #    enable = feature.split(b':')[1]
        #    self.non_stop = (enable == b'1')
        #    return self.create_rsp_packet(b"OK")

        else:
            return self.create_rsp_packet(b"")
        #EOF
    

    def get_registers(self):
        if (self._programming_state == 1):      # Workaround as we don't know how big the new program is
            self._programming_state = 0         # This was done before I figured out the memorymap .xml
            self.debugger.finalize_download()

        print("GDB request CPU registers")
        return self.create_rsp_packet(self.debugger.get_target_registers())
        #EOF
    

    def set_registers(self, data):
        print("GDB set CPU registers: {0}".format(data))
        if (b"xx" in data): # check if there is a register to ignore 
            return
        else:
            payload = int(data, 16)
            self.debugger.set_target_registers(payload)
    

    def handle_remote_command(self, cmd):
        """@brief Pass remote commands to the commander command processor."""

        if not isinstance(cmd, bytes):
            return self.create_rsp_packet(b'E01')

        if (cmd == b"reset halt"):
            print("GDB received remote reset halt cmd")
            self.debugger.reset_halt_Target()
            if (self.debugger.get_halt_status() == True):
                return self.create_rsp_packet(b'OK')
            else:
                return self.create_rsp_packet(b'E01')   # Reset failed
        else:
            print('GDB received Unknown remote command: {0}'.format(cmd))
            return self.create_rsp_packet(b'OK')


    def _get_resume_step_addr(self, data):
        if data is None:
            return None
        data = data.split(b'#')[0]
        if b';' not in data:
            return None
        # c[;addr]
        if data[0:1] in (b'c', b's'):
            addr = int(data[2:], base=16)
        # Csig[;addr]
        elif data[0:1] in (b'C', b'S'):
            addr = int(data[1:].split(b';')[1], base=16)
        #else:
        #    raise exceptions.DebugError("invalid step address received from gdb")
        return addr
        #EOF


    def resume(self, data):
        # addr = self._get_resume_step_addr(data)
        self.debugger.resume_Target()
        print("target resumed")

        if self.first_run_after_reset_or_flash:
            self.first_run_after_reset_or_flash = False

        val = b''

        # Timeout used only if the target starts returning faults. The is_running property of this timeout
        # also serves as a flag that a fault occurred and we're attempting to retry.
        #fault_retry_timeout = Timeout(self.session.options.get('debug.status_fault_retry_timeout'))

        #while fault_retry_timeout.check():
        while True:
            if self.shutdown_event.is_set():
                self.packet_io.interrupt_event.clear()
                return self.create_rsp_packet(val)

            self.lock.release()

            # Wait for a ctrl-c to be received.
            if self.packet_io.interrupt_event.wait(0.01):
                self.lock.acquire()
                print("GDB received CTRL-C")
                self.packet_io.interrupt_event.clear()

                # Be careful about reading the target state. If we previously got a fault (the timeout
                # is running) then ignore the error. In all cases we still return SIGINT.
                try:
                    self.debugger.halt_Target()
                    print("Target halted")
                    val = self.get_t_response(force_signal=0x02)
                except:
                    # Note: if the target is not actually halted, gdb can get confused from this point on.
                    # But there's not much we can do if we're getting faults attempting to control it.
                    val = b"S02"
                break

            self.lock.acquire()

            state = self.debugger.get_halt_status()
            if (state == True):
                val = self.get_t_response()
                break

        return self.create_rsp_packet(val)
        #EOF
    
    
    def step(self, data, start=0, end=0):
        print("GDB step: {0} (start=0x{1:02X}, end=0x{2:02X})".format(data, start, end))
        
        if (start == end):
            if (self.debugger.step_target() == True):
                #self.packet_io.send(self.create_rsp_packet(b"S05"))
                return self.create_rsp_packet(self.get_t_response(force_signal=0x05))
            else:
                return self.create_rsp_packet(b"E01")
        else:
            while (True):
                ret = self.debugger.step_target()
                if ret == False:
                    return self.create_rsp_packet(self.get_t_response(force_signal=0x05))
                else:
                    self.debugger.get_PC()
                    print("Current PC:0x{0}".format(self.debugger.target_pc))
                    if (self.debugger.target_pc in range(start, end)):
                        return self.create_rsp_packet(self.get_t_response(force_signal=0x05))
                
                if self.packet_io.interrupt_event.wait(0.01):
                    print("GDB received CTRL-C")
                    self.packet_io.interrupt_event.clear()
                    return self.create_rsp_packet(self.get_t_response(force_signal=0x05))
        #EOF




    def get_memory(self, data):
        split = data.split(b',')
        start = int(split[0], 16)
        length = split[1].split(b'#')[0]
        length = int(length, 16)

        print("GDB get Memory: addr=0x{0:x} len={1}".format(start, length))

        if (length == 0) and (start == 0):
            return self.create_rsp_packet(b"OK")

        elif (start in range(0x0000, 0x10000)): # Flash
            ret = self.debugger.read_target_flash(start, length)
            response = ""
            for x in ret:
                response += "{0:02X}".format(x)
            return self.create_rsp_packet(response.encode('ascii'))
        
        elif (start in range (0x8000, 0x10000)):  # Mapped PROGMEM, ".rodata"
            ret = self.debugger.read_target_flash(start - 0x8000, length)
            response = ""
            for x in ret:
                response += "{0:02X}".format(x)
            return self.create_rsp_packet(response.encode('ascii'))

        elif (start in range (0x800000, 0x808000)): # I/O, Periph, RAM
            ret = self.debugger.read_device_mem8(start - 0x800000, length)
            response = ""
            for x in ret:
                response += "{0:02X}".format(x)
            return self.create_rsp_packet(response.encode('ascii'))
        
        elif (start in range (0x808000, 0x810000)):  # Text data area
            ret = self.debugger.read_target_flash(start - 0x808000, length)
            response = ""
            for x in ret:
                response += "{0:02X}".format(x)
            return self.create_rsp_packet(response.encode('ascii'))

        else:
            return self.create_rsp_packet(b"E01")


    def write_memory(self, data):
        cmd = data[0:-3]
        arg, payload = cmd.split(b':')
        start, length = arg.split(b',')
        payload = unescape(payload)
        start = int(start, 16)
        length = int(length, 16)
        print("GDB Write Binary Data Start: 0x{0:04X}, Len: {1}, Data:".format(start, length))
        
        output = ""
        for x in range(0, length):
            if ((x % 16) == 0) and (x > 0):
                output += "\n"
            output += "{0:02x} ".format(payload[x])
        print(output)

        if (length == 0) and (start == 0):
            if (self._programming_state == 0):
                print("GDB Write Entering Programming Mode")
                self._programming_state = 1
                return self.create_rsp_packet(b"OK")
            else:
                return self.create_rsp_packet(b"E01")

        elif (start in range(0x0000, 0x10000)): # Flash
            if (self._programming_state == 1):
                self.debugger.prepare_target_flash(start, payload)
                return self.create_rsp_packet(b"OK")
            elif (length == 2):     # GDB wants to set a breakpoint, probably
                pass 
            return self.create_rsp_packet(b"E01")


        elif (start in range (0x800000, 0x808000)): # I/O, Periph, RAM
            return self.create_rsp_packet(b"E01")

        else:
            return self.create_rsp_packet(b"E01")
        #EOF


    def write_register(self, data):
        reg, val = data.split(b'=') # split and remove '=' from query
        val = val.split(b'#')[0]
        reg_num = int(reg, 16)
        val_len = len(val)
        
        
        value = int(val[0:2], 16)

        if (val_len >= 4):
            value += int(val[2:4], 16) << 8
        
        if (val_len >= 6):  # 24 bit max
            value += int(val[4:6], 16) << 16

        print("GDB Writing To Register {0} the value {1:04X}".format(reg_num, value))
        ret_val = self.debugger.set_target_register(reg_num, value)
        if (ret_val == True):
            return self.create_rsp_packet(b"OK")
        else:
            return self.create_rsp_packet(b"E13")   # Error Access

    
    def read_register(self, data):
        reg_num = int(data[0:2])
        reg_val = self.create_rsp_packet(self.debugger.get_target_register(reg_num))
        print("GDB Rading Register {0}: {1:02X}".format(reg_num, reg_val))
        return reg_val
    
    
    def breakpoint(self, data):
        # handle breakpoint/watchpoint commands
        split = data.split(b'#')[0].split(b',')
        addr = int(split[1], 16)
        print("GDB breakpoint {0}{1} @ {2}".format(data[0:1], int(data[1:2]), addr))

        # handle software breakpoint Z0/z0
        if data[1:2] == b'0':
            if data[0:1] == b'Z':
                if self.debugger.set_hw_breakpoint(0, addr):
                    return self.create_rsp_packet(b"OK")
            else:   # 'z'
                if self.debugger.clear_hw_breakpoint(0):
                    return self.create_rsp_packet(b"OK")
            return self.create_rsp_packet(b'E01') #EPERM

        # handle hardware breakpoint Z1/z1
        if data[1:2] == b'1':
            if data[0:1] == b'Z':
                if self.debugger.set_hw_breakpoint(1, addr):
                    return self.create_rsp_packet(b"OK")
            else:   # 'z'
                if self.debugger.clear_hw_breakpoint(1):
                    return self.create_rsp_packet(b"OK")
            return self.create_rsp_packet(b'E01') #EPERM

        return self.create_rsp_packet(b'E01') #EPERM
        #EOF
    

    def decode_hex_string(self, data, endian = "little") -> int:
        ret_val = 0
    
        length = len(data)
        n = 0
        pos = 0
        while (n < length):
            num = int(data[n:n+2], 16) & 0xFF
            n += 2
            if (endian == "little"):
                ret_val += num << (8*pos)
            else:
                ret_val = (ret_val << 8) + num
            
            pos += 1

        return ret_val
        #EOF
    
    
    def get_uint32_from_buf(buf, pos:int = 0, endian = "little"):
        retval = 0
        if (endian == "little"):
            retval  = (buf[pos + 0] & 0xFF) <<  0
            retval |= (buf[pos + 1] & 0xFF) <<  8
            retval |= (buf[pos + 2] & 0xFF) << 16
            retval |= (buf[pos + 3] & 0xFF) << 24
        elif (endian == "big"):
            retval  = (buf[pos + 0] & 0xFF) << 24
            retval |= (buf[pos + 1] & 0xFF) << 16
            retval |= (buf[pos + 2] & 0xFF) <<  8
            retval |= (buf[pos + 3] & 0xFF) <<  0
        print(buf)
        print(retval)
        return retval
    #EOC











def checksum(data: bytes) -> bytes:
    return ("%02x" % (sum(data) % 256)).encode()


CTRL_C = b'\x03'

class gdbserver_socket_io_thread(threading.Thread):
    """@brief Packet I/O thread.

    This class is a thread used by the GDBServer class to perform all RSP packet I/O. It
    handles verifying checksums, acking, and receiving Ctrl-C interrupts. There is a queue
    for received packets. The interface to this queue is the receive() method. The send()
    method writes outgoing packets to the socket immediately.
    """

    ## 100 ms timeout for socket and receive queue reads.
    RECEIVE_TIMEOUT = 0.1

    def __init__(self, port:int, event_queue:queue.Queue):
        super().__init__()
        self._port = port
        self._conn = None
        self._receive_queue = queue.Queue()
        self._event_queue = event_queue
        self._shutdown_event = threading.Event()
        self.interrupt_event = threading.Event()
        self.conn_close_event = threading.Event()
        self.send_acks = True
        self._clear_send_acks = False
        self._buffer = b''
        self._expecting_ack = False
        self.drop_reply = False
        self._last_packet = b''
        self._closed = False
        self.setDaemon(True)
        self.start()

    def set_send_acks(self, ack):
        if ack:
            self.send_acks = True
        else:
            self._clear_send_acks = True

    def stop(self):
        self._shutdown_event.set()

    def send(self, packet):
        if self._closed or not packet:
            return
        if not self.drop_reply:
            self._last_packet = packet
            self._write_packet(packet)
            print("Response: {0}".format(packet))
        else:
            self.drop_reply = False

    def receive(self, block=True):
        if self._closed:
            self.stop()
        while True:
            try:
                # If block is false, we'll get an Empty exception immediately if there
                # are no packets in the queue. Same if block is true and it times out
                # waiting on an empty queue.
                return self._receive_queue.get(block, self.RECEIVE_TIMEOUT)
            except queue.Empty:
                # Only exit the loop if block is false or connection closed.
                if not block:
                    return None
                if self._closed:
                    self.stop()

    def run(self):
        print("Starting GDB server packet I/O thread")
        
        sock = socket.create_server(('localhost', self._port), backlog=2)
        self._conn, addr = sock.accept()
        
        print("Client connected to port {0}!".format(self._port))
        while not self._shutdown_event.is_set():
            try:
                data = self._conn.recv(2048)

                # Handle closed connection
                if len(data) == 0:
                    print("GDB packet thread: other side closed connection")
                    self._closed = True
                    break

                self._buffer += data
            except (ConnectionAbortedError, ConnectionResetError) as err:
                print("GDB packet thread: connection unexpectedly closed during receive ({0})".format(err))
                self._closed = True
                break
            except socket.timeout:
                # Ignore timeouts.
                pass
            except OSError as err:
                print("Error in packet IO thread: {0}".format(err))

            if self._shutdown_event.is_set():
                break

            self._process_data()
            #EOL
        
        print("Client disconnected from port {0}!".format(self._port))
        self.send(b"$D#44")
        self._event_queue.put("disconnect")
        self._conn.close()
        self.stop()
    #EOF

    def _write_packet(self, packet):

        # Make sure the entire packet is sent.
        try:
            remaining = len(packet)
            while remaining:
                written = self._conn.send(packet)
                remaining -= written
                if remaining:
                    packet = packet[written:]
        except (ConnectionAbortedError, ConnectionResetError) as err:
            LOG.warning("GDB packet thread: connection unexpectedly closed during send (%s)", err)
            self._closed = True

        if self.send_acks:
            self._expecting_ack = True

    def _check_expected_ack(self):
        # Handle expected ack.
        c = self._buffer[0:1]
        if c in (b'+', b'-'):
            self._buffer = self._buffer[1:]
            if c == b'-':
                # Handle nack from gdb
                self._write_packet(self._last_packet)
                return

            # Handle disabling of acks.
            if self._clear_send_acks:
                self.send_acks = False
                self._clear_send_acks = False
        else:
            LOG.debug("GDB: expected n/ack but got '%s'", c)

    def _process_data(self):
        """@brief Process all incoming data until there are no more complete packets."""
        while len(self._buffer):
            if self._expecting_ack:
                self._expecting_ack = False
                self._check_expected_ack()

            # Check for a ctrl-c.
            if len(self._buffer) and self._buffer[0:1] == CTRL_C:
                print("GDB Received interrupt, Payload: {0}".format(self._buffer[1:]))
                self.interrupt_event.set()
                self._buffer = self._buffer[1:]

            try:
                # Look for complete packet and extract from buffer.
                pkt_begin = self._buffer.index(b"$")
                pkt_end = self._buffer.index(b"#") + 2
                if pkt_begin >= 0 and pkt_end < len(self._buffer):
                    pkt = self._buffer[pkt_begin:pkt_end + 1]
                    self._buffer = self._buffer[pkt_end + 1:]
                    self._handling_incoming_packet(pkt)
                else:
                    break
            except ValueError:
                # No complete packet received yet.
                break


    def _handling_incoming_packet(self, packet):
        # Compute checksum
        (data, cksum) = packet[1:].split(b'#')
        computedCksum = checksum(data)
        goodPacket = (computedCksum.lower() == cksum.lower())

        if self.send_acks:
            ack = b'+' if goodPacket else b'-'
            self._conn.send(ack)

        if goodPacket:
            self._receive_queue.put(packet)
    #EOF
#EOC