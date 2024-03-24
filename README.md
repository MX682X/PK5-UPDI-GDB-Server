# Arduino IDE GDB Server for UPDI Debugging
 Python Script to start a debugging session with the manufacturer's ICDs

Disclaimers:
1. I tried to avoid any trade-marketed terms, as I'm not affiliated with them,  so don't be surprised for my choice of words
2. I tried to write this whole thing real quick, couldn't be a big deal, right? Ended up taking longer then expected.
3. I have to focus on something else right now, this is why this is not finished yet.
3. I'm no Python programmer, so the syntax is not the best.
4. Still has a couple of bugs, but works more or less. (Breakpoints, CPU registers, Stepping, Flash Up- and Downloading)
5. needs pyusb, libusb_package and ElementTree python package to work
6. Consider this more as a proof of concept then anything else
7. Gonna need some expanding to work with more then the AVRxxDD28/DD32.
8. You'll need a copy of avr-gdb.exe with XML support. One is distributed with the Studio
9. Big thanks to pyOCD's gdbserver code, as without it, it would have taken way longer.
10. To start a gdb session, execute pk_dgb.py


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
debug.cortex-debug.custom.gdbTarget=localhost:50000
debug.cortex-debug.custom.postLaunchCommands.0=set remote hardware-watchpoint-limit 2
debug.cortex-debug.custom.postLaunchCommands.1=set breakpoint auto-hw off
```
