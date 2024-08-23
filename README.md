# Arduino IDE GDB Server for UPDI Debugging
 Python Script to start a debugging session with the manufacturer's ICDs

Things to know:
1. I tried to avoid any trade-marketed terms, as I'm not affiliated with them,  so don't be surprised for my choice of words
2. I'm no experienced Python programmer, so don't expect much code wise
3. There might be some bugs, but I hope I've ironed out most.
  - Known bugs: The Arduino debugger plug-in seems to hang after resetting the target
  - Supporting only the two hardware breakpoints, no software breakpoints (yet)
4. needs pyusb, libusb_package and ElementTree python package to work
5. You'll need a copy of avr-gdb.exe with XML support. One is distributed with the Studio. It needs to be copied to the compiler dictionary
6. To start a GDB session, execute e.g. `pk_gdbserver.py -pavr32dd28 -V5000 -b750 -a` in a command line
 - -p specifies the part name
 - -V when using a PK4/5 allows you to use the Power supply feature
 - -b specifies the UPDI Clock in kHz
 - -a keeps the session alive even if you stop it in the Arduino IDE (Allows you to upload new code without restarting the server)


Credit where credit is due:
- Big thanks to pyOCD's gdbserver code, as without it, it would have taken way longer to figure out gdb's inner workings


To Work with the Arduno IDE you must add following lines to your platform.txt:

```
debug.executable={build.path}/{build.project_name}.elf
debug.toolchain.prefix=avr-
debug.toolchain=gcc
debug.toolchain.path={compiler.path}
debug.server=external
debug.server.external.path={compiler.path}
debug.server.external.scripts_dir=
debug.server.external.script=
debug.cortex-debug.custom.device={build.mcu}
debug.cortex-debug.custom.gdbTarget=localhost:50000
debug.cortex-debug.custom.preLaunchCommands.0=set remote hardware-breakpoint-limit 2
#debug.cortex-debug.custom.showDevDebugOutput=raw
```
