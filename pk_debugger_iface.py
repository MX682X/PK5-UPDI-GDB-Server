# Copyright (c) 2026 @MX682X

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
# and associated documentation files (the "Software"), to deal in the Software without restriction 
# (except: selling it), including without limitation the rights to use, copy, modify, merge, 
# publish, distribute, and/or sublicense copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN 
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


class target():
    def __init__(self, dev_id, flash_size, page_size, ram_start, ram_size, dev_name):
        self.dev_id = dev_id
        self.flash_size = flash_size
        self.page_size = page_size
        self.ram_start = ram_start
        self.ram_size = ram_size
        self.dev_name = dev_name


target_lut = {
#     DeviceID[0:2] | Flash | Page | RAM Off | RAM Len | Target Name
    target (0x1E9120,   2048,    64,   0x3F80,      128, "ATtiny214"),
    target (0x1E9121,   2048,    64,   0x3F80,      128, "ATtiny212"),
    target (0x1E9122,   2048,    64,   0x3F80,      128, "ATtiny204"),
    target (0x1E9123,   2048,    64,   0x3F80,      128, "ATtiny202"),
    target (0x1E9220,   4096,    64,   0x3F00,      256, "ATtiny417"),
    target (0x1E9221,   4096,    64,   0x3F00,      256, "ATtiny416"),
    target (0x1E9222,   4096,    64,   0x3F00,      256, "ATtiny414"),
    target (0x1E9223,   4096,    64,   0x3F00,      256, "ATtiny412"),
    target (0x1E9225,   4096,    64,   0x3F00,      256, "ATtiny406"),
    target (0x1E9226,   4096,    64,   0x3F00,      256, "ATtiny404"),
    target (0x1E9227,   4096,    64,   0x3F00,      256, "ATtiny402"),
    target (0x1E922A,   4096,    64,   0x3E00,      512, "ATtiny427"),
    target (0x1E922B,   4096,    64,   0x3E00,      512, "ATtiny426"),
    target (0x1E922C,   4096,    64,   0x3E00,      512, "ATtiny424"),
    target (0x1E9320,   8192,    64,   0x3E00,      512, "ATtiny817"),
    target (0x1E9321,   8192,    64,   0x3E00,      512, "ATtiny816"),
    target (0x1E9322,   8192,    64,   0x3E00,      512, "ATtiny814"),
    target (0x1E9323,   8192,    64,   0x3E00,      512, "ATtiny807"),
    target (0x1E9324,   8192,    64,   0x3E00,      512, "ATtiny806"),
    target (0x1E9325,   8192,    64,   0x3E00,      512, "ATtiny804"),
    target (0x1E9326,   8192,    64,   0x3C00,     1024, "ATmega808"),
    target (0x1E9327,   8192,    64,   0x3C00,     1024, "ATtiny827"),
    target (0x1E9328,   8192,    64,   0x3C00,     1024, "ATtiny826"),
    target (0x1E9329,   8192,    64,   0x3C00,     1024, "ATtiny824"),
    target (0x1E932A,   8192,    64,   0x3C00,     1024, "ATmega809"),
    target (0x1E932C,   8192,    64,   0x7800,     2048, "AVR8EA28"),
    target (0x1E9420,  16384,    64,   0x3800,     2048, "ATtiny1617"),
    target (0x1E9421,  16384,    64,   0x3800,     2048, "ATtiny1616"),
    target (0x1E9422,  16384,    64,   0x3800,     2048, "ATtiny1614"),
    target (0x1E9423,  16384,    64,   0x3C00,     1024, "ATtiny1607"),
    target (0x1E9424,  16384,    64,   0x3C00,     1024, "ATtiny1606"),
    target (0x1E9425,  16384,    64,   0x3C00,     1024, "ATtiny1604"),
    target (0x1E9426,  16384,    64,   0x3800,     2048, "ATmega1609"),
    target (0x1E9427,  16384,    64,   0x3800,     2048, "ATmega1608"),
    target (0x1E9428,  16384,    64,   0x3800,     2048, "ATtiny1627"),
    target (0x1E9429,  16384,    64,   0x3800,     2048, "ATtiny1626"),
    target (0x1E942A,  16384,    64,   0x3800,     2048, "ATtiny1624"),
    target (0x1E9431,  16384,   512,   0x7800,     2048, "AVR16DD32"),
    target (0x1E9432,  16384,   512,   0x7800,     2048, "AVR16DD28"),
    target (0x1E9433,  16384,   512,   0x7800,     2048, "AVR16DD20"),
    target (0x1E9434,  16384,   512,   0x7800,     2048, "AVR16DD14"),
    target (0x1E9435,  16384,    64,   0x7800,     2048, "AVR16EA48"),
    target (0x1E9436,  16384,    64,   0x7800,     2048, "AVR16EA32"),
    target (0x1E9449,  16384,    64,   0x7800,     2048, "AVR16EB14"),
    target (0x1E9521,  32768,   128,   0x3800,     2048, "ATtiny3216"),
    target (0x1E9526,  32768,   128,   0x3400,     3072, "ATtiny3227"),
    target (0x1E9527,  32768,   128,   0x3400,     3072, "ATtiny3226"),
    target (0x1E9528,  32768,   128,   0x3400,     3072, "ATtiny3224"),
    target (0x1E9530,  32768,   128,   0x3000,     4096, "ATmega3208"),
    target (0x1E9531,  32768,   128,   0x3000,     4096, "ATmega3209"),
    target (0x1E9532,  32768,   512,   0x7000,     4096, "AVR32DA48"),
    target (0x1E9533,  32768,   512,   0x7000,     4096, "AVR32DA32"),
    target (0x1E9534,  32768,   512,   0x7000,     4096, "AVR32DA28"),
    target (0x1E9535,  32768,   512,   0x7000,     4096, "AVR32DB48"),
    target (0x1E9536,  32768,   512,   0x7000,     4096, "AVR32DB32"),
    target (0x1E9537,  32768,   512,   0x7000,     4096, "AVR32DB28"),
    target (0x1E9538,  32768,   512,   0x7000,     4096, "AVR32DD32"),
    target (0x1E9539,  32768,   512,   0x7000,     4096, "AVR32DD28"),
    target (0x1E953A,  32768,   512,   0x7000,     4096, "AVR32DD20"),
    target (0x1E953B,  32768,   512,   0x7000,     4096, "AVR32DD14"),
    target (0x1E953C,  32768,    64,   0x7000,     4096, "AVR32EA48"),
    target (0x1E953D,  32768,    64,   0x7000,     4096, "AVR32EA32"),
    target (0x1E953E,  32768,    64,   0x7000,     4096, "AVR32EA28"),
    target (0x1E9612,  65536,   512,   0x6000,     8192, "AVR64DA64"),
    target (0x1E9613,  65536,   512,   0x6000,     8192, "AVR64DA48"),
    target (0x1E9614,  65536,   512,   0x6000,     8192, "AVR64DA32"),
    target (0x1E9615,  65536,   512,   0x6000,     8192, "AVR64DA28"),
    target (0x1E9616,  65536,   512,   0x6000,     8192, "AVR64DB64"),
    target (0x1E9617,  65536,   512,   0x6000,     8192, "AVR64DB48"),
    target (0x1E9618,  65536,   512,   0x6000,     8192, "AVR64DB32"),
    target (0x1E9619,  65536,   512,   0x6000,     8192, "AVR64DB28"),
    target (0x1E961A,  65536,   512,   0x6000,     8192, "AVR64DD32"),
    target (0x1E961B,  65536,   512,   0x6000,     8192, "AVR64DD28"),
    target (0x1E961C,  65536,   512,   0x6000,     8192, "AVR64DD20"),
    target (0x1E961D,  65536,   512,   0x6000,     8192, "AVR64DD14"),
    target (0x1E961E,  65536,   128,   0x6800,     6144, "AVR64EA48"),
    target (0x1E961F,  65536,   128,   0x6800,     6144, "AVR64EA32"),
    target (0x1E9620,  65536,   128,   0x6800,     6144, "AVR64EA28"),
    target (0x1E9650,  49152,   128,   0x2800,     6144, "ATmega4808"),
    target (0x1E9651,  49152,   128,   0x2800,     6144, "ATmega4809"),
    target (0x1E9707, 131072,   512,   0x4000,    16384, "AVR128DA64"),
    target (0x1E9708, 131072,   512,   0x4000,    16384, "AVR128DA48"),
    target (0x1E9709, 131072,   512,   0x4000,    16384, "AVR128DA32"),
    target (0x1E970A, 131072,   512,   0x4000,    16384, "AVR128DA28"),
    target (0x1E970B, 131072,   512,   0x4000,    16384, "AVR128DB64"),
    target (0x1E970C, 131072,   512,   0x4000,    16384, "AVR128DB48"),
    target (0x1E970D, 131072,   512,   0x4000,    16384, "AVR128DB32"),
    target (0x1E970E, 131072,   512,   0x4000,    16384, "AVR128DB28"),
}


register_lut = [
#    Name, Index, bitsize,     type,  gdb_group,  gdb_type, gdb_num, gdb_feature
   [ "r0",     0,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r1",     1,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r2",     2,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r3",     3,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r4",     4,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r5",     5,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r6",     6,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r7",     7,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r8",     8,       8,   "lower", "general",   "uint8",    None,       None],
   [ "r9",     9,       8,   "lower", "general",   "uint8",    None,       None],
   ["r10",    10,       8,   "lower", "general",   "uint8",    None,       None],
   ["r11",    11,       8,   "lower", "general",   "uint8",    None,       None],
   ["r12",    12,       8,   "lower", "general",   "uint8",    None,       None],
   ["r13",    13,       8,   "lower", "general",   "uint8",    None,       None],
   ["r14",    14,       8,   "lower", "general",   "uint8",    None,       None],
   ["r15",    15,       8,   "lower", "general",   "uint8",    None,       None],
   ["r16",    16,       8,  "higher", "general",   "uint8",    None,       None],
   ["r17",    17,       8,  "higher", "general",   "uint8",    None,       None],
   ["r18",    18,       8,  "higher", "general",   "uint8",    None,       None],
   ["r19",    19,       8,  "higher", "general",   "uint8",    None,       None],
   ["r20",    20,       8,  "higher", "general",   "uint8",    None,       None],
   ["r21",    21,       8,  "higher", "general",   "uint8",    None,       None],
   ["r22",    22,       8,  "higher", "general",   "uint8",    None,       None],
   ["r23",    23,       8,  "higher", "general",   "uint8",    None,       None],
   ["r24",    24,       8,  "higher", "general",   "uint8",    None,       None],
   ["r25",    25,       8,  "higher", "general",   "uint8",    None,       None],
   ["r26",    26,       8,  "higher", "general",   "uint8",    None,       None],
   ["r27",    27,       8,  "higher", "general",   "uint8",    None,       None],
   ["r28",    28,       8,  "higher", "general",   "uint8",    None,       None],
   ["r29",    29,       8,  "higher", "general",   "uint8",    None,       None],
   ["r30",    30,       8,  "higher", "general",   "uint8",    None,       None],
   ["r31",    31,       8,  "higher", "general",   "uint8",    None,       None],
# CPU Extra Registers
  ["SREG",    32,       8,  "higher", "general",   "uint8",    None,       None],
   [ "SP",    33,      16,  "higher", "general","data_ptr",    None,       None],
   ["PC2",    34,      32,  "higher", "general","code_ptr",    None,       None],
# Pseudo Reg? Not quite sure what avr-gdb needs that one for
#   [ "pc",    35,      32,  "higher", "general",   "uint8",    None,       None],

# I wish I could add these, but GDB does not allow that. 
# Pseudo Regs for easier readability
#   [ "rX",    32,      16, "pointer",  "system", "data_ptr",   None,       None],
#   [ "rY",    33,      16, "pointer",  "system", "data_ptr",   None,       None],
#   [ "rZ",    34,      16, "pointer",  "system", "data_ptr",   None,       None],
]



import threading
import libusb_package
import usb.util, usb.core
from time import sleep
from xml.etree import ElementTree as ET
from enum import Enum

import scripts_dict as scr_dict


class UnknownPart(Exception):
    # Raised when a part name can not be found in the target_lut
    pass

class UnknownScript(Exception):
    # Raised when there is no correspnding script set to talk to the target
    pass

class ErrorXML(Exception):
    # Raised when we failed to generte an XML File
    pass

class NoDebugger(Exception):
    # Raised when no debugger was found in the USB devices
    pass

class CommunicationFailure(Exception):
    # Raised whenever we don't get a response from a debugger
    pass

def get_uint32_from_buf(buf:bytearray, pos:int, endian = "little"):
    retval = 0
    if (endian == "little"):
        retval |= (buf[pos + 0] & 0xFF) <<  0
        retval |= (buf[pos + 1] & 0xFF) <<  8
        retval |= (buf[pos + 2] & 0xFF) << 16
        retval |= (buf[pos + 3] & 0xFF) << 24
    elif (endian == "big"):
        retval  = (buf[pos + 0] & 0xFF) << 24
        retval |= (buf[pos + 1] & 0xFF) << 16
        retval |= (buf[pos + 2] & 0xFF) <<  8
        retval |= (buf[pos + 3] & 0xFF) <<  0
    return retval


def uint32_to_buf(num:int):
    buffer = bytearray(4)
    buffer[0] = (num >>  0) & 0xFF
    buffer[1] = (num >>  8) & 0xFF
    buffer[2] = (num >> 16) & 0xFF
    buffer[3] = (num >> 24) & 0xFF
    return buffer



probeMode = Enum("probeMode", ["OFF", "PROG", "DEBUG", "TO_Write", "TO_Read"])
targetState = Enum("targetState", ["OFF", "HALT", "RUN", "ERASED"])

class pk_debugger(threading.Thread):
    script_cmd_type = 0x0100
    script_upload_type = 0x80000102
    script_download_type = 0x0C0000101

    def __init__(self, part:str, voltage:int, baud:int):
        if ((voltage in range (1800, 5500)) and (voltage != 0) and (voltage != None)):
            self._voltage = voltage
        else:
            self._voltage = 0
        
        if((baud != None) and (baud in range(10, 900))): 
            self._updi_speed = baud
        else:
            self._updi_speed = 200
        
        self.part = part.upper()
        self._devID = 0x00
        self._revision = 0x00
        self._target:target = None

        # scripts
        self.scripts = dict()
        self.sib = ""
        self.nvm_version = ""

        # USB
        self._vid =  0x04D8
        self._pid = (0x9036, 0x9012)
        self._icd = None
        self._apVersion = ""
        self._serialNum = ""


        # EP Numbers, same for PK4 and PK5
        self._cmd_read_ep   = 0x81      # 129 == EP IN  1
        self._cmd_write_ep  = 0x02      #   2 == EP OUT 2
        self._data_read_ep  = 0x83      # 131 == EP IN  3
        self._data_write_ep = 0x04      #   4 == EP OUT 4

        # ADC Readings (in mV/mC/mA)
        self.internalVdd     = 0
        self.TargetVdd       = 0
        self.TargetVpp       = 0
        self.InternalVpp     = 0
        #self.VddSense        = 0  # Defaults to 0
        #self.Temp            = 0  # Temp defaults to 25°C
        self.VddCurrentSense = 0
        self.VddVoltageSense = 0


        # memory map: [Name:str,   from:int,   to:int]
        self._target_xml = ""
        self._memory_map_xml = ""

        self._target_regs = bytearray(32)
        self._target_sp = 0
        self.target_pc = 0
        self._targetState = targetState.OFF
        self._target_attached = False
        self._target_halt_status = 0x00
        self.target_flash_erased = 0
        self._new_program = bytearray(0x1FFFF)  # 128k parts
        self._program_tail = 0

        self._probeMode = probeMode.OFF
        self._probePowered = False  # True if Voltage supplied by debugger

        #EOF
    
    def init_debugger(self):
        if self.find_icd() == None:
            raise NoDebugger()
        if self._set_cpu(self.part) != 0:
            raise UnknownPart()
        if self._set_dev_info(self.part) != 0:
            raise UnknownScript()
        if self._create_target_xml() != 0:
            raise ErrorXML()
        if self._create_mem_map_xml() != 0:
            raise ErrorXML()
        

    def check_connection(self):
        if self.get_Firmware_Info() != 0:
            raise CommunicationFailure



    def _set_dev_info(self, part_name:str):
        part_name = part_name.upper()
        for dev in target_lut:
            if (part_name == dev.dev_name):
                self._target = dev
                return 0
        return -1

    def _create_target_xml(self):
        if (self._target_xml != ""):    # create once only
            return -1

        if (self._target is None):
            return -1

        xml_header = b"""<?xml version="1.0"?><!DOCTYPE target SYSTEM "gdb-target.dtd">"""
        tree_root = ET.Element("target")
        avr_arch = "avr:103"
        if self._target.flash_size == 65536:
            avr_arch = "avr:102"
        if self._target.flash_size == 131072:
            avr_arch = "avr:104"
        tree_arch = ET.SubElement(tree_root, "architecture").text = avr_arch
        tree_comp = ET.SubElement(tree_root, "compatible").text = "avr"
        tree_feat = ET.SubElement(tree_root, "feature", name="org.gnu.avr8.profile") # Placeholder profile name

        for reg in register_lut:
            ET.SubElement(tree_feat, "reg", name=reg[0], bitsize=str(reg[2]), regnum=str(reg[1]), type=reg[5])
        
        print("INFO: Generated target.xml")
        self._target_xml = xml_header + ET.tostring(tree_root)
        return 0
        #EOF

    def _create_mem_map_xml(self):
        if (self._memory_map_xml != ""):    # Generate only once
            return -1

        if (self._target == None):     # we need to know our target first
            return -1
        
        xml_header = b"""<?xml version="1.0"?><!DOCTYPE memory-map PUBLIC "+//IDN gnu.org//DTD GDB Memory Map V1.0//EN" "http://sourceware.org/gdb/gdb-memory-map.dtd">"""
        
        tree_root = ET.Element("memory-map")
        ram_start_hex = "80{0:04x}".format(self._target.ram_start)     # GDB expects RAM to start at 0x80 0000
        ram_length_hex = "{0:x}".format(self._target.ram_size)
        ET.SubElement(tree_root, "memory", type="ram", start=ram_start_hex, length=ram_length_hex)


        flash_length_hex = "{0:x}".format(self._target.flash_size)      # Flash starts at 0x00, the opposite compared to AVR debugging
        flash_map = ET.SubElement(tree_root, "memory", type="flash", start="00", length=flash_length_hex)
        blocksize = ET.SubElement(flash_map, "property", name="blocksize").text = "{0:x}".format(self._target.page_size)
        
        
        print("INFO: Generated memory_map.xml")
        self._memory_map_xml = xml_header + ET.tostring(tree_root)
        return 0
        #EOF
    
    def _set_cpu(self, cpu:str):
        cpu_str = cpu.upper()
        if cpu_str in scr_dict.scripts:
            self.scripts = scr_dict.scripts[cpu_str]
            print("Scripts for {0} found.".format(cpu_str))
            return 0
        else:
            print("Scripts for {0} not found. Allowed names are:".format(cpu_str))
            for x in scr_dict.scripts:
                print(x)
            return -1
    
    def find_icd(self):
        if self._icd is not None:
            return self._icd
        
        devices = list(libusb_package.find(find_all=1))
        #print(f'Found {len(devices)} USB-Devices in the system')

        icd = None
        for pid in self._pid:
            icd = libusb_package.find(idVendor=self._vid, idProduct=pid)
            if icd is not None:
                self._icd = icd
                return icd

        #print("No Debugger found by VID/PID")
        
        return None
        #EOF        

    
    def software_reset(self):
        self.run_Script(self.script_cmd_type, bytearray(0), [0xE7], 0)
        self.read_response("Software Reset")


    def recover_script(self):
        recover_cmd = 0x0107
        transfer = self.create_msg_header(recover_cmd, 16, 0x00)
        self._icd.write(self._cmd_write_ep, transfer)
        
        self.read_response("recover script")


    def set_PTG_mode(self, enabled:int):
        ptg_mode_array = [0x5E, bool(enabled), 0x00, 0x00, 0x00]
        response_length = 4
        self.run_Script(self.script_upload_type, bytearray(0), ptg_mode_array, response_length)

        self.read_response("Set PTG Mode")
        self.read_script_upload(response_length, "Set PTG Mode")
        self.send_script_done("Set PTG Mode")


    def get_Firmware_Info(self):
        self._icd.write(self._cmd_write_ep, [0xE1])
        ret = self._icd.read(self._cmd_read_ep, 1024, 25)
        if (ret[0] != 0xE1):
            print('ERROR: Wrong Device Response On "Get Firmware Info". Repose: \n' + ret)
            return -1

        self._apVersion = "apVer: {0:02X}.{1:02X}.{2:02X}, ".format(ret[3],ret[4],ret[5])

        self._serialNum = "serialNumber: "
        for x in range(32, 50):
            self._serialNum += chr(ret[x])

        return 0
        #EOF


    def set_live_connect(self, connect:int):
        if (self._probeMode == probeMode.OFF):
            set_live_conn_script = [0x39, bool(connect)]
            self.run_Script(self.script_cmd_type, bytearray(0), set_live_conn_script, 0)

            self.read_response("Set Live Connect")
        #EOF


    def set_Voltage (self, mVoltTarget:int):    # 0x40
        if (mVoltTarget == 0):
            self.run_Script(self.script_cmd_type, bytearray(0), [0x44], 0)
            if (0x00 == self.read_response("Shutdown Power")[0]):
                self._probeMode == probeMode.OFF
                self._targetState == targetState.OFF
        else:
            if (self._probeMode == probeMode.OFF):
                setVoltageCmd  = [0x40]
                setVoltageCmd += uint32_to_buf(mVoltTarget)  # (uint32_t) Vdd
                setVoltageCmd += uint32_to_buf(mVoltTarget)  # (uint32_t) Vpp operation
                setVoltageCmd += uint32_to_buf(mVoltTarget)  # (uint32_t) Vpp_op
                setVoltageCmd += [0x42, 0x43]
                self.run_Script(self.script_cmd_type, bytearray(0), setVoltageCmd, 0)

                self.read_response("Enable Power System")
            else:
                print("ERROR: Power System can be only enabled while detached")
        #EOF


    def select_power_source(self, internal:int):        # 0x46
        power_source = [0x46, bool(internal), 0x00, 0x00, 0x00]
        
        self.run_Script(self.script_cmd_type, bytearray(0), power_source, 0)
        self.read_response("Select Power Source")
        #EOF


    def get_Voltages(self):                             # 0x47
        getVoltagesCmd = [0x47]
        self.run_Script(self.script_cmd_type, bytearray(0), getVoltagesCmd, 0)
        ret = self.read_response("Read voltages")[1]

        self.internalVdd     = get_uint32_from_buf(ret, 0)
        self.TargetVdd       = get_uint32_from_buf(ret, 4)
        self.TargetVpp       = get_uint32_from_buf(ret, 8)     
        self.InternalVpp     = get_uint32_from_buf(ret, 12)     # probably HV Reset Voltage source
        #VddSense        = get_uint32_from_buf(ret, 16)  # Returned 0
        #Temp            = get_uint32_from_buf(ret, 20)  # Temp defaults to 25°C
        self.VddCurrentSense = get_uint32_from_buf(ret, 24)
        self.VddVoltageSense = get_uint32_from_buf(ret, 28)


        print("internalVdd: " + str(self.internalVdd) + "mV")
        print("TargetVdd: " + str(self.TargetVdd) + "mV")
        print("TargetVpp: " + str(self.TargetVpp) + "mV")
        print("InternalVpp: " + str(self.InternalVpp) + "mV")
        #print("VddSense: " + str(VddSense) + "mV")
        #print("Temp: " + str(Temp) + "mC")
        print("VddCurrentSense: " + str(self.VddCurrentSense) + "mA")
        print("VddVoltageSense: " + str(self.VddVoltageSense) + "mV")
        #EOF


    def set_LED_Brightness(self, brightness:int):
        LedBrightnessCmd = [0xCF, (0xFF & (brightness-1))]
        self.run_Script(self.script_cmd_type, bytearray(0), LedBrightnessCmd, 0)
        self.read_response("set_LED_Brightness")
        #EOF


    def set_UPDI_Speed(self, speed:int):
        print("Setting UPDI speed to {0}kHz".format(speed))
        self.run_Script(self.script_cmd_type, uint32_to_buf(speed), self.scripts["SetSpeed"], 0)
        self.read_response("Set UPDI Speed")
        #EOF


    def enter_Prog_Mode(self):
        if (self._probeMode == probeMode.DEBUG):
            self.exit_Debug_Mode()

        if (self._probeMode != probeMode.PROG):
            self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["EnterProgMode"], 0)
            ret = self.read_response("Enter Programming Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.PROG
                print("INFO: Entered PROG mode")
        else:
            print("ERROR: Can't enter PROG mode, Target mode not OFF")
        #EOF


    def exit_Prog_Mode(self):
        if (self._probeMode == probeMode.PROG):
            self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["ExitProgMode"], 0)
            ret = self.read_response("Exit Program Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.OFF
                print("INFO: Left PROG mode")
        else:
            print("ERROR: Can't leave PROG mode, Target not in PROG Mode")
        #EOF


    def enter_Debug_Mode(self):
        if (self._probeMode == probeMode.PROG):
            self.exit_Prog_Mode()
        
        if (self._probeMode != probeMode.DEBUG):
            self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["EnterDebugMode"], 0)
            ret = self.read_response("Enter Debug Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.DEBUG
                #self._target_halt_status = 0xAAAAAAAA
                print("INFO: Entered DEBUG mode")
        else:
            print("ERROR: Can't enter DEBUG mode, Target mode not OFF")
        #EOF


    def exit_Debug_Mode(self):
        if (self._probeMode == probeMode.DEBUG):
            self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["ExitDebugMode"], 0)
            ret = self.read_response("Exit Debug Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.OFF
                print("INFO: Left DEBUG mode")
        else:
            print("ERROR: Can't leave DEBUG mode, Target not in DEBUG Mode")
        #EOF


    def halt_Target(self):
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["Halt"], 0)
        ret = self.read_response("Halt Target")[0]
        if (ret == 0x00):
            self._targetState = targetState.HALT
            return True
        else:
            return False
        #EOF


    def resume_Target(self):
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["Run"], 0)
        ret = self.read_response("Resume Target")[0]
        if (ret == 0x00):
            self._targetState = targetState.RUN
            return True
        else:
            return False
        #EOF


    def get_halt_status(self):  # Returns True if halted
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["GetHaltStatus"], 0)
        ret = self.read_response("Halt Status")[1]
        new_hs = get_uint32_from_buf(ret, 0)
        if (self._target_halt_status != new_hs): 
            print("Halt Status returned: {0:04x}".format(new_hs))

        self._target_halt_status = new_hs
        if new_hs == 0xAAAAAAAA:
            return True
        else:
            return False
        #EOF



    def reset_Target(self): # Will halt automatically
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["DebugReset"], 0)
        return self.read_response("Reset Target")[0]    # 0x00 is good


    def reset_halt_Target(self):
        self.halt_Target()
        return self.reset_Target()


    def hold_in_reset(self):
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["HoldInReset"], 0)
        return self.read_response("hold in reset")[0]    # 0x00 is good


    def release_from_reset(self):
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["ReleaseFromReset"], 0)
        return self.read_response("release reset")[0]    # 0x00 is good


    def get_runtime_data(self):
        runtime = [0x1E, 0x00]
        self.run_Script(self.script_upload_type, bytearray(0), runtime, 0)
        self.read_response("runtime data")
        self.read_script_upload(0, "runtime data")
        self.send_script_done("runtime data")


    def set_hw_breakpoint(self, num:int, addr:int):
        param = uint32_to_buf(num)
        param += uint32_to_buf(addr)
        self.run_Script(self.script_cmd_type, param, self.scripts["SetHWBP"], 0)
        ret = self.read_response("Set HW breakpoint")[0]
        if ret != 0x00:
            print("ERROR: Failed setting HW breakpoint {0} at addr {1:04X}".format(num, addr))
            return False
        return True
        #EOF


    def clear_hw_breakpoint(self, num:int):
        param = uint32_to_buf(num)
        self.run_Script(self.script_cmd_type, param, self.scripts["ClearHWBP"], 0)
        ret = self.read_response("Clear HW breakpoint")[0]
        if ret != 0x00:
            print("ERROR: Failed clearing HW breakpoint {0}".format(num))
            return False
        return True
        #EOF


    def step_target(self):
        self.run_Script(self.script_cmd_type, [], self.scripts["SingleStep"], 0)
        ret = self.read_response("Single Step")[0]
        if ret != 0x00:
            print("ERROR: Failed Stepping to next instruction")
            return False
        return True
        

    def get_PC(self):
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["GetPC"], 0)
        ret = self.read_response("get_PC")[1]

        self.target_pc = get_uint32_from_buf(ret, 0)
        #print("Current PC: {0:06X}".format(self.target_pc))
        return ret, self.target_pc   # get byte (LE) representation, and integer
        #EOF


    def set_PC(self, value):
        param = bytearray(4)
        if (isinstance(value, int)):
            param = uint32_to_buf(value)
        elif (isinstance(value, bytearray)):
            param = value
        else:
            print("ERROR, Wrong Data Type in Set PC")
            return
        
        param_len = len(param)
        if param_len != 4:
            print("ERROR: Wrong bytearray length passed: {0}".format(param_len))
            return

        if self._target == None:
            print("ERROR: Target must be known to Write PC to it")
            return
        
        flash_size = self._target.flash_size
        flash_mask = (flash_size >> 9) - 1  # Max PC is half the Flash size
        param[3] = 0x00     # make sure to have valid inputs only
        param[2] = 0x00
        
        if (param[1] > flash_mask):
            print("ERROR: PC bigger then Flash Size")
            return
            
        self.run_Script(self.script_cmd_type, param, self.scripts["SetPC"], 0)
        ret = self.read_response("set_PC")[0]
        if ret == 0x00:
            return True
        else:
            return False
        #EOF


    def get_SP_SREG(self):
        return self.read_target_mem8(0x3D, 3)
        #EOF

    
    def get_target_ID(self, force:bool = False):
        if (self._devID == 0x00) or (force is True):
            self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["GetDeviceID"], 0)
            ret = self.read_response("Get Target ID")[1]
            revision = ret[3]
            devID = ret[0] << 16 | ret[1] << 8 | ret[2]

            self._devID             = devID
            self._revision          = revision
            print("Device ID: {0:06X}".format(devID))
        #EOF


    def check_BIST(self):
        key = b"BIST Tested"
        self.get_Status_From_String(key, "check BIST")

        key = b"BIST Results"
        self.get_Status_From_String(key, "check BIST")


    def get_Target_Id(self):
        self.enter_Prog_Mode()
        #self.check_BIST()
        self.get_target_ID()
        self.exit_Prog_Mode()


    def get_ocd_regs(self):
        data = self.read_target_mem8(0xF80, 12)
        hwbpa  = get_uint32_from_buf(data, 0)
        hwbpb  = get_uint32_from_buf(data, 4)
        print("HWBP: 0x{0:04X} | 0x{1:04X}, 0x{2:02X}, 0x{3:02X}, 0x{4:02X}, 0x{5:02X}, "\
              .format(hwbpa, hwbpb, data[8], data[9], data[10], data[11]))


    def get_probe_status(self):
        get_key = [
            0x9B, 0x00, 0x07,       # load into reg 0x00 the int 0x07 (ASI_KEY_STATUS)
            0x1E, 0x0E, 0x00,       # load CS reg
            0x9F,                   # copy data to return
            0x9B, 0x00, 0x0B,       # load into reg 0x00 the int 0x0B (ASI_SYS_STATUS)
            0x1E, 0x0E, 0x00,       # load CS reg
            0x9F,                   # copy data to return
        ]
        message = self.create_msg_header(self.script_cmd_type, 24+len(get_key), 0)
        message += self.create_script_header(0, len(get_key))
        message += bytearray(get_key)
        try:
            self._icd.write(self._cmd_write_ep, message, 1000)
        except usb.core.USBTimeoutError:
            return probeMode.TO_Write
        
        ret_val = probeMode.OFF
        try:
            ret = self._icd.read(self._cmd_read_ep, 1024, 1000)
            ret_status = get_uint32_from_buf(ret, 16)
            if (ret_status == 0x00):
                data_len   = ret[20]
                if (data_len == 0x02):
                    if ret[24] == 0x02:
                        ret_val = probeMode.DEBUG
                    elif ret[25] == 0x08:
                        ret_val = probeMode.PROG
            ret_val = probeMode.OFF
        except usb.core.USBTimeoutError:
            ret_val = probeMode.TO_Read
            try:
                self.recover_script()
            except:
                pass
        return ret_val


    def create_msg_header(self, type:int, message_len:int, transfer_len:int):
        header  = uint32_to_buf(type)
        header += uint32_to_buf(0)      # Always 0
        header += uint32_to_buf(message_len)
        header += uint32_to_buf(transfer_len)
        return header


    def create_script_header(self, arg_len:int, script_len:int):
        scr_header  = uint32_to_buf(arg_len)
        scr_header += uint32_to_buf(script_len)
        return scr_header


    def run_Script(self, type:int, scr_params:bytearray, script:bytearray, transfer_len:int):
        if (self._icd == None):
            raise NoDebugger

        script_len = len(script)
        param_len = len(scr_params)
        header_len = 16 + 8
        preamble_len = header_len + param_len
        message_len = preamble_len + script_len
        transfer = bytearray(message_len)
        transfer[ 0:16] = self.create_msg_header(type, message_len, transfer_len)
        transfer[16:24] = self.create_script_header(param_len, script_len)

        for x in range (0, param_len):
            transfer[header_len + x] = scr_params[x]
        
        for x in range (0, script_len):
            transfer[preamble_len + x] = script[x]

        try: 
            self._icd.write(self._cmd_write_ep, transfer)
        except:
            print("Script write failed, trying to reset")
            self.recover_script()

        #EOF


    def read_response(self, func:str, timeout:int = 1000):
        try: 
            ret = self._icd.read(self._cmd_read_ep, 1024, timeout)
            response_status = get_uint32_from_buf(ret, 0)
            if (response_status != 0x0D):
                raise ValueError("Wrong Device Response On '" + func + "'. Repose: {0}".format(ret))
        except:
            print("Read response failed, trying to reset")
            self.recover_script()
            return


        ret_len = get_uint32_from_buf(ret, 8)
        ret_status = get_uint32_from_buf(ret, 16)
        data_len   = get_uint32_from_buf(ret, 20)

        if (ret_len == 0x10):
            return [0x00, []]

        elif (ret_len < 24):
            
            pass
        else:
            data = bytearray(data_len)
            if (data_len > 0):
                data = ret[24:24+data_len]
        
        if (ret_status == 0x0104):
            print("WARNING: Write to Register Failed. Chip must be halted first")
        elif (ret_status != 0x00):
            print("WARNING: Status is not 0: {0:04x}".format(ret_status))

        return [ret_status, data]
        #EOF


    def read_script_upload(self, expected_len:int, func:str):
        if (self._icd == None):
            raise NoDebugger
        ret = self._icd.read(self._data_read_ep, expected_len, 1000)
        return ret
        #EOF


    def write_script_download(self, data:bytearray, func:str):
        if (self._icd == None):
            raise NoDebugger
        self._icd.write(self._data_write_ep, data)


    def send_script_done(self, func:str):
        if (self._icd == None):
            raise NoDebugger
        script_done_type = 0x0103  # == 259
        transfer = self.create_msg_header(script_done_type, 16, 0)
        self._icd.write(self._cmd_write_ep, transfer)

        self.read_response(func)
        #EOF


    def get_Status_From_String(self, key:bytes, func:str):
        if (self._icd == None):
            raise NoDebugger
        
        type = 0x0105
        if (key[-1:] != 0x00):
            key += b"\x00"  # Add String NULL terminator if there is none
        message_len = 16 + len(key) + 1 

        transfer = self.create_msg_header(type, message_len, 0)
        transfer += key

        self._icd.write(self._cmd_write_ep, transfer)
        ret = self._icd.read(self._cmd_read_ep, 1024, 250)
        response_status = get_uint32_from_buf(ret, 0)
        
        if (response_status != 0x0D):
            print("ERROR: bad Response")
        
        status_len = get_uint32_from_buf(ret, 8)
        status = ret[16:status_len] # No Terminating NULL

        return bytes(status)
        #EOF


    def get_memory_map_xml(self):
        return self._memory_map_xml
        #EOF


    def get_target_xml(self):
        return self._target_xml
        #EOF


    def conv_byte_to_hex(self, byte:int):
        byte = byte & 0xFF
        first = (byte // 16) + 0x30
        if first > 0x39:
            first += 0x07
        
        sec = (byte & 0x0F) + 0x30
        if sec > 0x39:
            sec += 0x07
        return chr(first)+chr(sec)


    def get_target_registers(self):
        #read_len = end - start + 1
        #if start not in range(0, 32) or end not in range(0, 32):
        #    raise ValueError ("Register Numbers out of range. Start: {0}, End: {1}".format(start, end))
        #if read_len not in range(1, 33):
        #    raise ValueError ("Register Range out of Bounds. Start: {0}, End: {1}".format(start, end))
        cpu_regs = self.read_target_mem8(0, 32) # limit to all CPU regs for now 
        sreg_sp = self.read_target_mem8(0x3D, 3)
        cpu_pc = self.get_PC()[1] * 2

        ret_val = ""
        #for x in range (0, start):
        #    ret_val += "xx"                 # Unread registers
        for x in range (0, 32):
            ret_val += self.conv_byte_to_hex(cpu_regs[x])
        #for x in range (read_len, 32):
        #    ret_val += "xx"                 # Unread registers
        
        # X, Y and Z (RIP)
        #if (start <= 26 and end >= 27):
        #ret_val += self.conv_regval_to_hex(regs[26]) + self.conv_regval_to_hex(regs[27]) 
        #else:
        #    ret_val += "xxxx"
        #if (start <= 28 and end >= 29):
        #ret_val += self.conv_regval_to_hex(regs[28]) + self.conv_regval_to_hex(regs[29])
        #else:
        #    ret_val += "xxxx"
        #if (start <= 30 and end >= 31):
        #ret_val += self.conv_regval_to_hex(regs[30]) + self.conv_regval_to_hex(regs[31])
        #else:
        #    ret_val += "xxxx"
        
        # SREG, SP, PC2
        ret_val += self.conv_byte_to_hex(sreg_sp[2])
        ret_val += self.conv_byte_to_hex(sreg_sp[0]) + self.conv_byte_to_hex(sreg_sp[1]) 
        ret_val += self.conv_byte_to_hex((cpu_pc >>  0) & 0xFF)
        ret_val += self.conv_byte_to_hex((cpu_pc >>  8) & 0xFF)
        ret_val += self.conv_byte_to_hex((cpu_pc >> 16) & 0xFF)
        ret_val += self.conv_byte_to_hex((cpu_pc >> 24) & 0xFF)
        return ret_val.encode("ascii")


    def set_target_registers(self, data:bytes):
        data_len = len(data)
        expected_len = 32 + 1 + 2 + 4
        if (data_len < expected_len):
            print("ERROR, received registers are too short")
            return
        if (data_len > expected_len):
            print("ERROR, received registers are too long")
            return
        
        addr = 4000     # == 0x0FA0. Undocumented Memory area between SYSCFG and NVMCTRL. 0xF80 seems to be OCD module address
        self.write_target_mem8(addr, data[0:32])    # CPU Regs, all in one go
        self.write_target_mem8(0x3F, data[32:33])   # SREG
        self.write_target_mem8(0x3D, data[33:35])   # SP
        self.set_PC(data[35:39])                    # PC


    def get_target_register(self, reg:int):
        if reg in range(0, 32):
            val &= 0xFF
            addr = 4000 + reg
            param = [val]
            # self.read_target_mem8(addr, param)
        elif reg == 32:     # SREG
            val &= 0xFF
            addr = 0x3F
            param = [val]
            # self.read_target_mem8(addr, param)
        elif reg == 33:     # SP
            addr = 0x3D
            param = [val & 0xFF, (val>>8) & 0xFF]
            # self.read_target_mem8(addr, param)
        elif reg == 34:
            self.get_PC()
        else:
            print("ERROR: unknown register to get: {0}". format(reg))


    def set_target_register(self, reg:int, val:int):
        was_halted = self.get_halt_status() # There is a case when GDB w
        if (was_halted == False):
            self.halt_Target()

        if reg in range(0, 32):
            val &= 0xFF
            addr = 4000 + reg
            param = [val]
            ret_val = self.write_target_mem8(addr, param)
        elif reg == 32:     # SREG
            val &= 0xFF
            addr = 0x3F
            param = [val]
            ret_val = self.write_target_mem8(addr, param)
        elif reg == 33:     # SP
            addr = 0x3D
            param = [val & 0xFF, (val>>8) & 0xFF]
            ret_val = self.write_target_mem8(addr, param)
        elif reg == 34:
            ret_val = self.set_PC(val)
        else:
            print("ERROR: unknown register to set: {0}". format(reg))
            ret_val = False

        if (was_halted == False):
            self.resume_Target()
        return ret_val
        #EOF


    def read_target_flash(self, start:int, len:int):
        len_mod = (len - (len % 512) + 512) # read in 512 byte chunks
        start_modulo = (start % 512)
        start_mod = start - start_modulo
        
        param = uint32_to_buf(0x800000 + start_mod)
        param += uint32_to_buf(len_mod)

        self.run_Script(self.script_upload_type, param, self.scripts["ReadProgmem"], len_mod)
        self.read_response("Read Program Memory")
        ret = self.read_script_upload(len_mod, "Read Program Memory")
        self.send_script_done("Read Program Memory")
        flash_read = ret[start_modulo:(start_modulo+len)]
        return flash_read


    def prepare_target_flash(self, start:int, data:bytes):
        #if (self._targetState != targetState.ERASED):
        #    return False    # Abort, Target, not ready to be written to
        #self.enter_Debug_Mode()
        data_len = len(data)
        

        # Fill "empty" space with 0xFF
        #fill = 0xFF
        #fill = fill.to_bytes(1, 'little')
        for x in range (self._program_tail, start):
            self._new_program[x] = 255
            self._program_tail += 1

        for y in range (0, data_len):
            self._new_program[start+y] = data[y]
            self._program_tail += 1
        #EOF


    def finalize_download(self):
        if (self.erase_target_flash() == False):
            return False

        self.prepare_target_flash(((self._program_tail // 1024) + 1) * 1024, [])    # Fill up

        self.enter_Prog_Mode()  
        
        transfers = self._program_tail // 1024
        print("INFO: Starting Programming: Transfer count: {0}, Program Length: {1}". format(transfers, self._program_tail))

        param = uint32_to_buf(0x800000)
        param += uint32_to_buf(self._program_tail)

        # Start Programming
        self.run_Script(self.script_download_type, param, self.scripts["WriteProgmem"], self._program_tail)
        self.read_response("Download Program")

        # Program Flash, split transfer to 4k chunks
        tail_iterator = 0
        total_length = self._program_tail
        while (total_length > 1024):
            new_tail = tail_iterator+1024
            self._icd.write(self._data_write_ep, self._new_program[tail_iterator:new_tail], 10000)
            tail_iterator = new_tail
            total_length -= 1024
        self._icd.write(self._data_write_ep, self._new_program[tail_iterator:self._program_tail], 10000)
        
        # Check for Errors
        key = b"ERROR_STATUS_KEY"
        ret = self.get_Status_From_String(key, "Download Program")
        self.send_script_done("Download Program")
        if not (ret.startswith(b"NONE")):
            print ("ERROR: Download Program failed, code: {0}".format(ret)) 

        downloaded_code = self.read_target_flash(0x00, self._program_tail)

        if (self._program_tail != len(downloaded_code)):
            print("WARNING: Different Code Sizes. Expected: {0}, Received: {1}".format(self._program_tail, len(downloaded_code)))
        else:
            failed = 0
            for x in range (self._program_tail):
                if (self._new_program[x] != downloaded_code[x]):
                    print("WARNING: PROGMEM discrepancy Found on pos {0}". format(x))
                    failed = 1
                    break
            if (failed == 0):
                print("INFO: Download Successful")
        
        self.target_flash_erased = 0
        self.exit_Prog_Mode()
        # Reset variables
        self._program_tail = 0

        self.enter_Debug_Mode()
        self.halt_Target()
        pass

        #EOF


    def erase_target_flash(self):
        if (self.target_flash_erased == 1):
            return True
        self.enter_Prog_Mode()
        print("INFO: Erasing Target")
        self.run_Script(self.script_cmd_type, bytearray(0), self.scripts["EraseChip"], 0)
        ret = self.read_response("Erase Chip")[0]
        self.exit_Prog_Mode()
        if ret == 0x00:
            self.target_flash_erased = 1
            return True
        else:
            return False
        #EOF


    def read_target_mem8(self, addr:int, read_len:int):
        param = uint32_to_buf(addr)
        param += uint32_to_buf(read_len)
        self.run_Script(self.script_upload_type, param, self.scripts["ReadMem8"], read_len)

        self.read_response("Read Target Mem8")
        ret = self.read_script_upload(read_len, "Read Target Mem8")   

        self.send_script_done("Read Target Mem8")
        return ret
        #EOF
    

    def write_target_mem8(self, addr:int, value:bytearray):
        if (self._probeMode != probeMode.DEBUG):
            print("ERROR: Attempt to write register memory outside Debug Mode")
            return False
        
        write_len = len(value)
        param = uint32_to_buf(addr)
        param += uint32_to_buf(write_len)

        self.run_Script(self.script_download_type, param, self.scripts["WriteMem8"], write_len)
        ret = self.read_response("Write Target Mem8")[0]
        if (ret != 0x00):
            print ("ERROR: Init Write Mem8 failed, code: {0}".format(ret))
            return False
        
        self._icd.write(self._data_write_ep, value)  # write new value to memory

        key = b"ERROR_STATUS_KEY"

        ret = self.get_Status_From_String(key, "Write Target Mem8")
        self.send_script_done("Write Target Mem8")
        if not (ret.startswith(b"NONE")):
            print ("ERROR: Download Program failed, code: {0}".format(ret)) 
            return False
        
        return True
        #EOF


    def attach_power(self):
        self.get_Voltages()                             # 0x47
        if (self.VddVoltageSense < 1000):  # Only power the system if there is no voltage already
            if (self._voltage >= 1800):
                self.select_power_source(True)          # 0x46
                self.set_Voltage(0)             # 0x44
                self.set_Voltage(self._voltage) # 0x40
            else:
                self.select_power_source(False)         # 0x46
                self.set_Voltage(0)             # 0x44
        self.get_Voltages()                             # 0x47
        if (self.VddVoltageSense in range (1800, 5500)):    # Assert Target Voltage 
            return 1
        else:
            print ("WANING: Target Voltage out of operational Range")
            return 0
        #EOF


    def attach_target(self):
        if self._target_attached == True:
            return
        self.get_Firmware_Info()                # 0xE1
        self.set_PTG_mode(False)                # 0x5E; 0x00
        self.set_live_connect(True)             # 0x39
        self.attach_power()
        self.set_UPDI_Speed(self._updi_speed)   # len 0x21
        self.get_Target_Id()
        self.enter_Debug_Mode()                 # len 0x6C
        self.halt_Target()                 # len 0x6C
        self._target_attached = True
        #EOF


    def detach_target(self):
        if (self._probeMode == probeMode.DEBUG):
            self.exit_Debug_Mode()          # len 0x1A
        elif (self._probeMode == probeMode.PROG):
            self.exit_Prog_Mode()
        self._targetState = targetState.OFF
        self.set_live_connect(False)        # 0x39
        self.set_Voltage(0)         # 0x44
        self._target_attached = False       # Always allow detatching


    def refresh_icd_status(self):
        self.get_Firmware_Info()                # 0xE1
        self.set_PTG_mode(False)                # 0x5E; 0x00
        self.set_live_connect(False)            # 0x39
        self.attach_power()
        self.set_LED_Brightness(5)              # 0xCF
        self.set_UPDI_Speed(self._updi_speed)   # len 0x21
        self.get_Target_Id()
        self.set_live_connect(False)
        self.set_Voltage(0)
        #EOF


    def live_connect_to_target(self):
        self.get_Firmware_Info()                    # 0xE1
        self.set_PTG_mode(False)                    # 0x5E; 0x00
        
        self.set_live_connect(True)                # 0x39

        if (self._voltage >= 1800):
            self.select_power_source(True)          # 0x46
            self.set_Voltage(0)             # 0x44
            self.set_Voltage(self._voltage) # 0x40  ToDo: Figure out live connect with disabled power supply
        else:
            self.select_power_source(False)         # 0x46
            self.set_Voltage(0)             # 0x44

        self.get_Voltages()                     # 0x47
        self.set_LED_Brightness(5)              # 0xCF
        self.set_UPDI_Speed(self._updi_speed)   # len 0x21
        self.get_Target_Id()
        self.enter_Debug_Mode()                 # len 0x6C
        self.halt_Target()                      # len 0x59
        self.get_halt_status()                  # len 0x59; 0x45
        self.get_PC()                           # len 0x3D
        self.read_target_mem8(0x3F, 1)          # len 0x33; 0x3F
        #EOF


    def reset_connected_target(self):
        self.reset_Target()                 # len 0x53
        self.get_PC()                       # len 0x3D
        self.read_target_mem8(0x3F)         # len 0x33
        #EOF


    def disconnect_from_target(self):
        self.exit_Debug_Mode()          # len 0x1A
        #self.get_Firmware_Info()        # 0xE1
        self.set_live_connect(True)     # 0x39
        self.set_Voltage(0)     # 0x44
#EOC
