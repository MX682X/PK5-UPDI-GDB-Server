#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.environ['PYUSB_DEBUG'] = 'warning'

import libusb_package

import usb.core
import usb.util
import array
from time import sleep
from _thread import *
import threading
import pk_gdbserver


# find our device


#pk5.set_configuration()

#gdb_socket = socket.create_server(('localhost', 50000))
#tcl_socket = socket.create_server(('localhost', 50001))
#telnet_socket = socket.create_server(('localhost', 50002))



print (
"    Welcome to the PK GDB Tool.\n\
    Type 'init' to start up server (at port 50000)\n\
    Type 'stop' to disable the power to the MCU, if supplied"
)

from pk_debugger_iface import pk_debugger
debugger = pk_debugger(3300)

gdb_ser = None

while True:
    user_in = input(">")
    if (user_in == "P"):
        if debugger.find_icd() is not None:
            debugger.refresh_icd_status()

    elif (user_in == "init"):
        #debugger.live_connect_to_device()
        gdb_ser = pk_gdbserver.gdb_server(50000, debugger)
    
    elif (user_in == "detach") or (user_in == "stop"):
        debugger.detach_target()

    elif (user_in.startswith("Volt")):
        debugger.get_Voltages()
    
    elif (user_in == ("refresh")):
        debugger.refresh_icd_status()
    
    elif (user_in == ("attach")):
        debugger.attach_target()
    
    elif (user_in.startswith("server")):
        port_in = user_in[6:]
        while ((len(port_in) > 0)  and (port_in[0].isdigit() == False)):
            port_in = port_in[1:]
        
        if (port_in.isdecimal() == False):
            raise ValueError("Bad input on Port, abort. Input: {0}, {1}".format(user_in, port_in))
        port_num = int(port_in)
        if port_num not in range (1024, 0xFFFF):
            raise ValueError("Port {0} out of range".format(port_num))
        else:
            print("Starting gdbserver on localhost, port {0}".format(port_num))
            gdb_ser = pk_gdbserver.gdb_server(port_num, debugger)
        #start_new_thread(server_thread, (port_num, ))

    elif (user_in == "q"):
        debugger.detach_target()
        if gdb_ser is not None:
            gdb_ser.stop()
        quit()
        
    sleep(0.1)
    #EOL

