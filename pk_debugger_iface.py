#!/usr/bin/env python3
# -*- coding: utf-8 -*-



EnterProgMode_UPDI_cmd = 0x00003000
EnterProgMode_UPDI = [      # len = 0x013E (345)
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x00, 0x1E, 0x01, 0x00, 
0x01, 0xFD, 0x19, 0x00, 0x00, 0x00, 0x08, 0x01, 
0x94, 0x32, 0x00, 
0x94, 0x40, 0x00, 
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 
0x6C, 0x01, 0x66, 0x01, 0x08, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x08, 0x00, 0x00, 0x00, 0x26, 0x01, 
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x59, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x01, 0x00, 
0x65, 0x20, 0x67, 0x6F, 0x72, 0x04, # NVMPROG Key (Little Endian)
0x65, 0x50, 0x4D, 0x56, 0x4E, 0x04, # 0x4E564D50726F6720
0x1E, 0x11, 0x01, 0x9B, 0x02, 0x07, 0x1E, 0x0E, 0x02, 
0x6C, 0x03, 0x66, 0x03, 0x10, 0x00, 0x00, 0x00, 
0x9B, 0x04, 0x10, 0xFC, 0x03, 0x04, 0x1E, 0x01, 
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x59, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x01, 0x0B, 0xA2, 0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x00, 0x1E, 0x0F, 0x00, 0x01,
0x9B, 0x01, 0x0B, 0xA2, 0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x94, 0x48, 0x00, 0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 
0x6C, 0x01, 0x66, 0x01, 0x08, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x08, 0x00, 0x00, 0x00, 0x26, 0x01, 
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 
0x6C, 0x01, 0x66, 0x01, 0x01, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x01, 0x00, 0x00, 0x00, 0x13, 0x01, 
0x6C, 0x01, 0x66, 0x01, 0x02, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x02, 0x00, 0x00, 0x00, 0x13, 0x01, 
0x9B, 0x01, 0x0C, 0x1E, 0x0E, 0x01, 
0x6C, 0x02, 0x66, 0x02, 0x04, 
0x00, 0x00, 0x00, 0xFE, 0x02, 0x04, 
0x00, 0x00, 0x00, 0x13, 0x01, 
0x94, 0xF4, 0x01, 
0x9B, 0x01, 0x0C, 0x1E, 0x0E, 0x01, 
0x6C, 0x02, 0x66, 0x02, 0x04, 
0x00, 0x00, 0x00, 0xFE, 0x02, 0x04, 
0x00, 0x00, 0x00, 0x13, 0x01, 0xFB, 0x1E, 0x01, 
0x90, 0x01, 0x51, 0x00, 0x00, 0x00, 0x7F, 0x01, 0xFB, 0x26, 0x01, 
0x90, 0x01, 0x44, 0x00, 0x00, 0x00, 0x7F, 0x01, 0xFB, 0x26, 0x01, 
0x90, 0x01, 0x00, 0x01, 0x00, 0x00, 0x7F, 0x01]


ExitProgMode_UPDI_cmd = 0x00003100
ExitProgMode_UPDI = [   # len = 0x2E (73)
0x9B, 0x00, 0x08, 0x9B, 0x01, 
0x59, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x00, 0x08, 0x9B, 0x01, 
0x00, 0x1E, 0x0F, 0x00, 0x01, 0x1E, 0x02]

SetSpeed_UPDI_cmd = 0x00001503
SetSpeed_UPDI = [
    0x91, 0x00, 0x1E, 0x14, 0x00 
    ]


GetDeviceID_UPDI_cmd = 0x00001505
GetDeviceID_UPDI = [    # len = 0x39 (84)
0x95, 0x90, 0x00, 0x00, 0x11, 0x00, 0x00, 0x1E, 0x09, 0x00, 
0x9C, 0x01, 0x03, 0x00, 0x1E, 0x10, 0x01, 
0x9B, 0x02, 0x03, 0x1E, 0x0C, 0x02, 
0x90, 0x02, 0x01, 0x0F, 0x00, 0x00, 0x1E, 0x03, 0x02, 0x9F]


EraseChip_UPDI_cmd = 0x00001200
EraseChip_UPDI = [      # len = 0xD0 (235)
0x94, 0x32, 0x00, 
0x94, 0x40, 0x00, 
0x90, 0x01, 0x00, 0x00, 0x00, 0x00, 
0x65, 0x65, 0x73, 0x61, 0x72, 0x04, # 0x65736172 - UPDI Chiperase Key, little Enidian
0x65, 0x45, 0x4D, 0x56, 0x4E, 0x04, # 0x454D564E ==> 0x4E564D4572617365
0x1E, 0x11, 0x01, 
0x90, 0x02, 0x07, 0x00, 0x00, 0x00, 
0x1E, 0x0E, 0x02, 0x6C, 0x03, 
0x66, 0x03, 0x08, 0x00, 0x00, 0x00, 0x90, 0x04, 
0x08, 0x00, 0x00, 0x00, 0xFC, 0x03, 0x04, 0xAF, 0x00, 
0x90, 0x00, 0x08, 0x00, 0x00, 0x00, 
0x90, 0x01, 0x59, 0x00, 0x00, 0x00, 
0x1E, 0x0F, 0x00, 0x01, 
0x90, 0x01, 0x0B, 0x00, 0x00, 0x00, 0xA2, 
0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x90, 0x00, 0x08, 0x00, 0x00, 0x00, 
0x90, 0x01, 0x00, 0x00, 0x00, 0x00, 
0x1E, 0x0F, 0x00, 0x01, 
0x90, 0x01, 0x0B, 0x00, 0x00, 0x00, 0xA2, 
0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x90, 0x01, 0x0B, 0x00, 0x00, 0x00, 0xA2, 
0x94, 0x02, 0x00, 
0x1E, 0x0E, 0x01, 
0xA5, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xF4, 0x01, 
0x1E, 0x0E, 0x01, 0x6C, 0x03, 0x66, 0x03, 0x40, 0x00, 0x00, 0x00, 
0xFE, 0x03, 0x40, 0x00, 0x00, 0x00, 0xAF, 0x00, 0xFB, 0xB7, 0x00, 
0x90, 0x01, 0x00, 0x01, 0x00, 0x00, 0x7F, 0x01, 0x5A]





WriteProgmem_UPDI = [   # len = 0x0130  (331)
0x91, 0x00, 0x91, 0x01, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x11, 0x00, 0x00, 0x00, 0x00, 
0x90, 0x0F, 0x00, 0x02, 0x00, 0x00, 0xFA, 0x01, 0x0F, 0x30, 0x00, 0x60, 0x0F, 0x01, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x08, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x90, 0x06, 0xFF, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x00, 0x06, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x02, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x90, 0x10, 0x00, 0x01, 0x00, 0x00, 0xFA, 0x0F, 0x10, 0xA8, 0x00, 
0x60, 0x10, 0x0F, 0x1E, 0x09, 0x00, 
0x60, 0x04, 0x10, 0x67, 0x04, 0x01, 0x1E, 0x10, 0x04, 0x1E, 0x0B, 0x04, 
0x6A, 0x0F, 0x10, 0x6E, 0x00, 0x10, 
0x6A, 0x01, 0x10, 0xFC, 0x0F, 0x11, 
0x9A, 0x00, 0x6C, 0x0C, 
0x90, 0x0D, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x0C, 0x0D, 0x00, 0x01, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 0xFC, 0x01, 0x11, 0x22, 0x00, 0x5A, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
]


ReadProgmem_UPDI = [    # len = 0x69 (132)
0x91, 0x00, 
0x91, 0x01, 
0x95, 0x90, 0x11, 0x00, 0x00, 0x00, 0x00, 
0x90, 0x0F, 0x40, 0x00, 0x00, 0x00, 
0xFA, 0x01, 0x0F, 0x19, 0x00, 
0x60, 0x0F, 0x01, 
0x90, 0x10, 0x00, 0x01, 0x00, 0x00, 
0xFA, 0x0F, 0x10, 0x27, 0x00, 
0x60, 0x10, 0x0F, 
0x1E, 0x09, 0x00, 0x60, 0x04, 0x10, 
0x67, 0x04, 0x01, 
0x1E, 0x10, 0x04, 
0x1E, 0x0D, 0x04, 
0x6A, 0x0F, 0x10, 
0x6E, 0x00, 0x10, 
0x6A, 0x01, 0x10, 
0xFC, 0x0F, 0x11, 0x19, 0x00, 
0xFC, 0x01, 0x11, 0x0B, 0x00 ] 


WriteDataEEmem_UPDI = [
0x91, 0x00, 
0x91, 0x01, 
0x60, 0x03, 0x01, 
0x93, 0x03, 0x01, 0x00, 0xAD, 0x03, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x13, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 0x1E, 0x09, 0x00, 
0x9C, 0x04, 0x01, 0x00, 0x1E, 0x10, 0x04, 0x1E, 0x0A, 0x04, 0x6C, 0x0C, 
0x90, 0x0D, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x0C, 0x0D, 0x7F, 0x00, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAE, 0x5A, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
]


ReadDataEEmem_UPDI = [
0x91, 0x00, 
0x91, 0x01, 0x60, 0x03, 0x01, 
0x93, 0x03, 0x01, 0x00, 
0x95, 0xAD, 0x03, 0x1E, 0x09, 0x00, 
0x9C, 0x04, 0x01, 0x00, 0x1E, 0x10, 0x04, 0x1E, 0x0C, 0x04, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAE, 0x5A, 
]


WriteConfigmem_UPDI = [
0x91, 0x00, 
0x91, 0x01, 0xAD, 0x01, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x13, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x99, 0x03, 0x1E, 0x06, 0x00, 0x03, 0x6C, 0x0C, 
0x90, 0x0D, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x0C, 0x0D, 0x70, 0x00, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAE, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
]


ReadConfigmem_UPDI = [      # len 0x33
0x91, 0x00, 
0x91, 0x01, 
0x95, 0xAD, 0x01, 0x1E, 0x03, 0x00, 0x9F, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 
0xAE, 0x5A
]
# ConfigMemFuse & ConfigMemLock are the same byte script, so I removed them
# Actually it is the same as ReadMem8


WriteIDmem_UPDI = [
0x91, 0x00, 
0x91, 0x01, 
0x60, 0x03, 0x01, 
0x93, 0x03, 0x20, 0x00, 0xAD, 0x03, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x08, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x90, 0x06, 0xFF, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x00, 0x06, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x02, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 0x1E, 0x09, 0x00, 
0x9C, 0x04, 0x20, 0x00, 0x1E, 0x10, 0x04, 0x1E, 0x0A, 0x04, 0x6C, 0x0C, 
0x90, 0x0D, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x0C, 0x0D, 0xD9, 0x00, 
0x90, 0x02, 0x02, 0x10, 0x00, 0x00, 0xA2, 0x1E, 0x03, 0x02, 
0x94, 0x02, 0x00, 0xA5, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14, 0x00, 
0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07, 
0x92, 0x00, 0x20, 0x00, 0x00, 0x00, 
0xAE, 0x5A, 0x90, 0x06, 0x00, 0x10, 0x00, 0x00, 
0x90, 0x07, 0x00, 0x00, 0x00, 0x00, 0x1E, 0x06, 0x06, 0x07
]


ReadIDmem_UPDI = [
0x91, 0x00, 
0x91, 0x01, 
0x60, 0x03, 0x01, 
0x93, 0x03, 0x01, 0x00, 0x95, 0xAD, 0x03, 
0x1E, 0x09, 0x00, 
0x9C, 0x04, 0x01, 0x00, 
0x1E, 0x10, 0x04, 0x1E, 0x0C, 0x04, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAE, 0x5A
]


WriteCSreg_UPDI_cmd = 0x00000215
WriteCSreg_UPDI = [
0x99, 0x00, 
0x99, 0x01, 0x1E, 0x0F, 0x00, 0x01
]


ReadCSreg_UPDI_cmd = 0x00000215
ReadCSreg_UPDI = [
0x99, 0x00, 0x1E, 0x0E, 0x00, 0x9F
]


WriteMem8_UPDI_cmd = 0x00000215
WriteMem8_UPDI = [
0x91, 0x00, 
0x91, 0x01, 
0xAD, 0x01, 0x99, 0x03, 0x1E, 0x06, 0x00, 0x03, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 0xAE, 0x5A, 
]


WriteMem16_UPDI_cmd = 0x00000215
WriteMem16_UPDI = [
0x91, 0x00, 
0x91, 0x01, 0x67, 0x01, 0x01, 
0xAD, 0x01, 0x9A, 0x03, 0x1E, 0x07, 0x00, 0x03, 
0x92, 0x00, 0x02, 0x00, 0x00, 0x00, 0xAE, 0x5A 
]


ReadMem8_UPDI_cmd = 0x00000215
ReadMem8_UPDI = [
0x91, 0x00, 
0x91, 0x01, 0x95, 
0xAD, 0x01, 0x1E, 0x03, 0x00, 0x9F, 
0x92, 0x00, 0x01, 0x00, 0x00, 0x00, 
0xAE, 0x5A
]


ReadMem16_UPDI_cmd = 0x00000215
ReadMem16_UPDI = [
0x91, 0x00, 
0x91, 0x01, 0x95, 0x67, 0x01, 0x01, 
0xAD, 0x01, 0x1E, 0x04, 0x00, 0x9D, 
0x92, 0x00, 0x02, 0x00, 0x00, 0x00, 0xAE, 0x5A, 
]


# System information Block
ReadSIB_UPDI_cmd = 0x00000215
ReadSIB_UPDI = [
0x95, 0x9B, 0x00, 0x02, 0x1E, 0x12, 0x00
]


EnterDebugMode_UPDI_cmd = 0x00000215
EnterDebugMode_UPDI = [ # len = 0x6C (135)
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x00, 0x1E, 0x01, 0x00, 0x01, # 0x9B 0x01 [0x00] - only difference between differen Debug Modes
0x94, 0xC8, 0x00, 
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 
0x6C, 0x01, 0x66, 0x01, 0x01, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x01, 0x00, 0x00, 0x00, 0x4B, 0x00, 
0x9B, 0x01, 0x00, 
0x65, 0x20, 0x20, 0x20, 0x20, 0x04, # 0x20202020  UPDI Debug Key
0x65, 0x20, 0x44, 0x43, 0x4F, 0x04, # 0x2044434F ==> "OCD     " (yes, with spaces)
0x1E, 0x11, 0x01, 
0x9B, 0x02, 0x07, 0x1E, 0x0E, 0x02, 0x6C, 0x03, 
0x66, 0x03, 0x02, 0x00, 0x00, 0x00, 
0xFE, 0x03, 0x02, 0x00, 0x00, 0x00, 0x53, 0x00, 
0x90, 0x01, 0x00, 0x01, 0x00, 0x00, 0x7F, 0x01, 0x5A
]




ExitDebugMode_UPDI_cmd = 0x00000215
ExitDebugMode_UPDI = [
     0x1E, 0x02 
     ]

#The same on each chip
Run_UPDI = [        # len = 0x54 (111)
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 0x1E, 0x0E, 0x00, 
0x6C, 0x02, 0x66, 0x02, 0x20, 0x00, 0x00, 0x00, 
0xFE, 0x02, 0x20, 0x00, 0x00, 0x00, # ] == UPDI Preamble?
0x33, 0x00, 0x90, 0x00, 0x88, 0x0F, 0x00, 0x00, 
0x9B, 0x01, 0x02, 0x1E, 0x06, 0x00, 0x01, 
0x9B, 0x00, 0x04, 
0x9B, 0x01, 0x02, 0x1E, 0x0F, 0x00, 0x01, 
0xFB, 0x3B, 0x00, # 0xFB == Delimiter, 0x003B == Length?, LE
0x90, 0x01, 0x00, 0x01, 0x00, 0x00, 
0x7F, 0x01, 0x5A ] 

#The same on each chip
Halt_UPDI = [
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 0x1E, 0x0E, 0x00, 
0x6C, 0x02, 0x66, 0x02, 0x20, 0x00, 0x00, 0x00, 
0xFE, 0x02, 0x20, 0x00, 0x00, 0x00, 
0x38, 0x00, 0x9B, 0x00, 0x04, 
0x9B, 0x01, 0x01, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x00, 0x05, 0xA2, 0x1E, 0x0E, 0x00, 
0xA5, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x64, 0x00, 
0xFB, 0x40, 0x00, 0x90, 0x01, 0x00, 0x01, 0x00, 0x00, 
0x7F, 0x01, 0x5A ]


#seems to be the same, need to check 128K
GetPC_UPDI_cmd = 0x8000140E
GetPC_UPDI = [      # len = 0x3D (88)
0x90, 0x00, 0x94, 0x0F, 0x00, 0x00, 
0x1E, 0x04, 0x00, 
0x6C, 0x01, 
0x1E, 0x15, 0x02, 0x03, 0x90, 0x04, 0x00, 0x00, 0x00, 0x00, # == UPDI PC Command
0xFC, 0x03, 0x04, 0x1D, 0x00, 
0x67, 0x01, 0x01, 
0x69, 0x01, 0x01, 0x00, 0x00, 0x00, 
0x98, 0x01 ]


SetPC_UPDI_cmd = 0x00000215
SetPC_UPDI = [      # len 0x71 (140)
0x91, 0x00, 
0x1E, 0x15, 0x02, 0x03, 0x90, 0x04, 0x00, 0x00, 0x00, 0x00, # == UPDI PC Command
0xFC, 0x03, 0x04, 0x14, 0x00, 0x68, 0x00, 0x01, 
0x90, 0x01, 0x94, 0x0F, 0x00, 0x00, 0x1E, 0x07, 0x01, 0x00, 
0x90, 0x02, 0x90, 0x0F, 0x00, 0x00, 
0x9C, 0x03, 0x00, 0x00, 0x1E, 0x07, 0x02, 0x03, 
0x90, 0x00, 0x88, 0x0F, 0x00, 0x00, 
0x9B, 0x01, 0x04, 0x1E, 0x06, 0x00, 0x01, 
0x9B, 0x00, 0x04, 
0x9B, 0x01, 0x02, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x00, 0x05, 0xA2, 0x1E, 0x0E, 0x00, 
0xA5, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 
0x0A, 0x00 ]



DebugReset_UPDI_cmd = 0x00000215
DebugReset_UPDI = [ # len = 0x53 (110)
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x59, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x01, 0x0B, 0xA2, 0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x9B, 0x00, 0x08, 
0x9B, 0x01, 0x00, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x01, 0x0B, 0xA2, 0x1E, 0x0E, 0x01, 
0xA5, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0A, 0x00, 
0x94, 0x40, 0x00]


GetHaltStatus_UPDI_cmd = 0x00000215
GetHaltStatus_UPDI = [  #len 0x45 (96)
0x90, 0x00, 0x05, 0x00, 0x00, 0x00, 0x1E, 0x0E, 0x00, 
0x6C, 0x01, 0x66, 0x01, 0x01, 0x00, 0x00, 0x00, 
0xFE, 0x01, 0x01, 0x00, 0x00, 0x00, 0x24, 0x00, 
0x90, 0x02, 0x55, 0x55, 0x55, 0x55, 0x98, 0x02, 
0xFB, 0x2C, 0x00, 0x90, 0x02, 0xAA, 0xAA, 0xAA, 0xAA, 
0x98, 0x02, 0x5A ]


SingleStep_UPDI_cmd = 0x00000215
SingleStep_UPDI = [     # len 0x65 (128)
0x9B, 0x00, 0x0B, 0x1E, 0x0E, 0x00, 0x1E, 0x0E, 0x00, 
0x6C, 0x02, 0x66, 0x02, 0x20, 0x00, 0x00, 0x00, 
0xFE, 0x02, 0x20, 0x00, 0x00, 0x00, 0x45, 0x00, 
0x90, 0x00, 0x88, 0x0F, 0x00, 0x00, 
0x9B, 0x01, 0x04, 0x1E, 0x06, 0x00, 0x01, 
0x9B, 0x00, 0x04, 
0x9B, 0x01, 0x02, 0x1E, 0x0F, 0x00, 0x01, 
0x9B, 0x00, 0x05, 0xA2, 0x1E, 0x0E, 0x00, 
0xA5, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x32, 0x00, 
0xFB, 0x4D, 0x00, 
0x90, 0x01, 0x00, 0x01, 0x00, 0x00,
0x7F, 0x01 ]

SetHWBP_UPDI_cmd = 0x00000215
SetHWBP_UPDI = [
0x91, 0x00, 
0x91, 0x01, 
0x90, 0x05, 0x01, 0x00, 0x00, 0x00, 
0xFA, 0x00, 0x05, 
0x9C, 0x00, 0x68, 0x01, 0x01, 
0x66, 0x01, 0xFE, 0xFF, 0xFF, 0xFF, 0x1E, 0x15, 0x02, 0x03, 
0xFE, 0x03, 0x00, 0x00, 0x00, 0x00, 0x2F, 0x00, 
0xFE, 0x03, 0x01, 0x00, 0x00, 0x00, 0x38, 0x00, 0xFB, 
0x9C, 0x00, 0x61, 0x01, 0x01, 0x00, 0x00, 0x00, 0xFB, 0x6B, 0x00, 
0x90, 0x05, 0x89, 0x0F, 0x00, 0x00, 0x1E, 0x03, 0x05, 
0x6C, 0x06, 0x60, 0x07, 0x00, 
0x92, 0x07, 0x01, 0x00, 0x00, 0x00, 0xFE, 0x01, 0x00, 0x00, 0x00, 0x00, 0x5E, 0x00, 
0x7C, 0x06, 0x07, 0x1E, 0x06, 0x05, 0x06, 0xFB, 0x6B, 0x00, 
0x6F, 0x07, 0xFF, 0xFF, 0xFF, 0xFF, 
0x7D, 0x06, 0x07, 0x1E, 0x06, 0x05, 0x06, 
0x90, 0x05, 0x80, 0x0F, 0x00, 0x00, 0x68, 0x00, 0x02, 
0x6E, 0x05, 0x00, 0x1E, 0x07, 0x05, 0x01, 
0x90, 0x06, 0x00, 0x80, 0x00, 0x00, 
0x90, 0x07, 0x01, 0x00, 0x01, 0x00, 
0xF9, 0x06, 0x07, 0x9C, 0x00, 0x92, 0x05, 0x02, 0x00, 0x00, 0x00, 0x60, 0x06, 0x01, 
0x67, 0x06, 0x10, 0x1E, 0x07, 0x05, 0x06, 0x5A ]


ClearHWBP_UPDI_cmd = 0x00000215
ClearHWBP_UPDI = [
0x91, 0x00, 
0x90, 0x01, 0x00, 0x00, 0x00, 0x00, 
0x90, 0x05, 0x01, 0x00, 0x00, 0x00, 
0xFA, 0x00, 0x05, 
0x88, 0x00, 0x68, 0x01, 0x01, 
0x66, 0x01, 0xFE, 0xFF, 0xFF, 0xFF, 0x1E, 0x15, 0x02, 0x03, 
0xFE, 0x03, 0x00, 0x00, 0x00, 0x00, 0x33, 0x00, 
0xFE, 0x03, 0x01, 0x00, 0x00, 0x00, 0x36, 0x00, 0xFB, 
0x88, 0x00, 0xFB, 0x57, 0x00, 
0x90, 0x05, 0x89, 0x0F, 0x00, 0x00, 0x1E, 0x03, 0x05, 0x6C, 0x06, 
0x60, 0x07, 0x00, 0x92, 0x07, 0x01, 0x00, 0x00, 0x00, 
0x6F, 0x07, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D, 0x06, 0x07, 0x1E, 0x06, 0x05, 0x06, 
0x90, 0x05, 0x80, 0x0F, 0x00, 0x00, 0x68, 0x00, 0x02, 
0x6E, 0x05, 0x00, 0x1E, 0x07, 0x05, 0x01, 
0x90, 0x06, 0x00, 0x80, 0x00, 0x00, 
0x90, 0x07, 0x01, 0x00, 0x01, 0x00, 0xF9, 0x06, 0x07, 
0x88, 0x00, 0x92, 0x05, 0x02, 0x00, 0x00, 0x00, 0x60, 0x06, 0x01, 
0x67, 0x06, 0x10, 0x1E, 0x07, 0x05, 0x06, 0x5A ]


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

# I wish I could add these, but GDP does not allow that. 
# Pseudo Regs for easier readability
#   [ "rX",    32,      16, "pointer",  "system", "data_ptr",   None,       None],
#   [ "rY",    33,      16, "pointer",  "system", "data_ptr",   None,       None],
#   [ "rZ",    34,      16, "pointer",  "system", "data_ptr",   None,       None],
]


device_lut = {  
#   ID [0:2]      Flash Len RAM Start  RAM Len   Pins      Arch   Device name
    0x1E9431   : (  0x8000,    0x7800,   0x800,   32, "avr:103", "AVR16DD32"),
    0x1E9432   : (  0x8000,    0x7800,   0x800,   28, "avr:103", "AVR16DD28"),

    0x1E9538   : (  0x8000,    0x7000,  0x1000,   32, "avr:103", "AVR32DD32"),
    0x1E9539   : (  0x8000,    0x7000,  0x1000,   28, "avr:103", "AVR32DD28"),

    0x1E961A   : ( 0x10000,    0x6000,  0x2000,   32, "avr:103", "AVR64DD32"),
    0x1E961B   : ( 0x10000,    0x6000,  0x2000,   28, "avr:103", "AVR64DD28"),
}
devlut_flash_len = 0
devlut_ram_start = 1
devlut_ram_len   = 2
devlut_pin_count = 3
devlut_arch      = 4
devlut_devname   = 5


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


import threading
import queue
import libusb_package
import usb.util
from time import sleep
from xml.etree import ElementTree as ET
from enum import Enum

probeMode = Enum("probeMode", ["OFF", "PROG", "DEBUG"])
targetState = Enum("targetState", ["OFF", "HALT", "RUN", "ERASED"])

class pk_debugger(threading.Thread):
    script_cmd_type = 0x0100
    script_upload_type = 0x80000102
    script_download_type = 0x0C0000101

    def __init__(self, voltage:int):
        self._voltage = 0
        if ((voltage in range (1800, 5100)) and (voltage != 0)):
            self._voltage = voltage
        else:
            print("Voltage request out of range, Disabling Powering the device")
        
        self._updi_speed = 200

        self._icd:usb.core.Device = None
        self.vid_pk4 =  0x03EB
        self.pid_pk4 = (0x2177, 0x2178, 0x2179, 0x217A)
        self.vid_pk5 =  0x04D8
        self.pid_pk5 = (0x9036,0x9035)
        self._icd = self.find_icd()

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
        self._devID = 0x00
        self._revision = 0x00
        self._device_info = None

        self._target_regs = bytearray(32)
        self._target_sp = 0
        self.target_pc = 0
        self._targetState = targetState.OFF
        self._target_attached = False
        self._target_halt_status = 0x00
        self.target_flash_erased = 0
        self._new_program = []
        self._program_tail = 0

        self._probeMode = probeMode.OFF
        self._probePowered = False  # True if Voltage supplied by debugger
        #EOF

    def _create_target_xml(self):
        if (self._target_xml != ""):    # create once only
            return
        
        if (self._devID == 0x00) and (self._probeMode != probeMode.OFF):
            self.get_Target_Id()    # Try to get the device info if not happend already

        if (self._device_info is None):
            return

        xml_header = b"""<?xml version="1.0"?><!DOCTYPE target SYSTEM "gdb-target.dtd">"""
        tree_root = ET.Element("target")
        tree_arch = ET.SubElement(tree_root, "architecture")
        tree_arch.text = self._device_info[devlut_arch]
        tree_comp = ET.SubElement(tree_root, "compatible")
        tree_comp.text = "avr"
        tree_feat = ET.SubElement(tree_root, "feature", name="org.gnu.avr8.profile") # Placeholder profile name

        for reg in register_lut:
            ET.SubElement(tree_feat, "reg", name=reg[0], bitsize=str(reg[2]), regnum=str(reg[1]), type=reg[5])
        
        print("INFO: Generated target.xml")
        self._target_xml = xml_header + ET.tostring(tree_root)
        #EOF



    def _create_mem_map_xml(self):
        # This doesn't work, GDB quits. :/
        if (self._memory_map_xml != ""):    # Generate only once
            return

        if (self._device_info == None):     # we need to know our device first
            return
        
        xml_header = b"""<?xml version="1.0"?><!DOCTYPE memory-map PUBLIC "+//IDN gnu.org//DTD GDB Memory Map V1.0//EN" "http://sourceware.org/gdb/gdb-memory-map.dtd">"""
        
        tree_root = ET.Element("memory-map")
        ram_start_hex = "80{0:04x}".format(self._device_info[devlut_ram_start])
        ram_length_hex = "{0:x}".format(self._device_info[devlut_ram_len])
        ET.SubElement(tree_root, "memory", type="ram", start=ram_start_hex, length=ram_length_hex)


        flash_length_hex = "{0:x}".format(self._device_info[devlut_flash_len])
        flash_map = ET.SubElement(tree_root, "memory", type="flash", start="00", length=flash_length_hex)
        blocksize = ET.SubElement(flash_map, "property", name="blocksize")
        # UPDI can only do chip erase.
        # It is possible to erase only a page, but ugh
        blocksize.text = flash_length_hex     
        
        
        print("INFO: Generated memory_map.xml")
        self._memory_map_xml = xml_header + ET.tostring(tree_root)
        #EOF

    
    def find_icd(self):
        if self._icd is not None:
            return self._icd
        
        devices = list(libusb_package.find(find_all=1))
        print(f'Found {len(devices)} USB-Devices in the system')

        icd = None
        for p in self.pid_pk5:
            icd = libusb_package.find(idVendor=self.vid_pk5, idProduct=p)
            if icd is not None:
                print("PK5 found")
                self._icd = icd
                return icd

        print("No PK5 found by VID/PID, trying to find PK4 next")
        for p in self.pid_pk4:
            icd = libusb_package.find(idVendor=self.vid_pk4, idProduct=p)
            if icd is not None:
                print("PK4 found")
                self._icd = icd
                return icd
        
        print("No PK4 found by VID/PID, Check connections and try again")
        return None
        #EOF        

     
    # 0x5E = enabledPTG, +(uint32_t)ProgrammerToGoMode
    # ->runScriptWithUpload -> doUpload -> readTransfer
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
            raise ValueError('Wrong Device Response On "Get Firmware Info". Repose: \n' + ret)

        apVersion = "apVer: {0:02X}.{1:02X}.{2:02X}, ".format(ret[3],ret[4],ret[5])
        deviceID = "devId: {0:02X}{1:02X}{2:02X}{3:02X}, ".format(ret[21], ret[20], ret[19], ret[18])

        # This typecasting took way too long to figure out....
        # Look what they need to mimick the power of C (printf("%s", &ret[32]))
        SerialNum = "serialNumber: "
        for x in range(32, 50):
            SerialNum += chr(ret[x])

        print(apVersion + deviceID + SerialNum)
        #EOF


    def set_live_connect(self, connect:int):
        if (self._probeMode == probeMode.OFF):
            set_live_conn_script = [0x39, bool(connect)]
            self.run_Script(self.script_cmd_type, bytearray(0), set_live_conn_script, 0)

            self.read_response("Set Live Connect")
        #EOF


    def enable_Power_System (self, mVoltTarget:int):    # 0x40
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


    def disable_Power_System(self):                     # 0x44
        self.run_Script(self.script_cmd_type, bytearray(0), [0x44], 0)
        if (0x00 == self.read_response("Shutdown Power")[0]):
            self._probeMode == probeMode.OFF
            self._targetState == targetState.OFF


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


    # speed in kHz
    def set_UPDI_Speed(self, speed:int):
        print("Setting UPDI speed to {0}kHz".format(speed))
        self.run_Script(self.script_cmd_type, uint32_to_buf(speed), SetSpeed_UPDI, 0)
        self.read_response("Set UPDI Speed")
        #EOF


    def enter_Prog_Mode(self):
        if (self._probeMode == probeMode.DEBUG):
            self.exit_Debug_Mode()

        if (self._probeMode != probeMode.PROG):
            self.run_Script(self.script_cmd_type, bytearray(0), EnterProgMode_UPDI, 0)
            ret = self.read_response("Enter Programming Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.PROG
                print("INFO: Entered PROG mode")
        else:
            print("ERROR: Can't enter PROG mode, Target mode not OFF")
        #EOF


    def exit_Prog_Mode(self):
        if (self._probeMode == probeMode.PROG):
            self.run_Script(self.script_cmd_type, bytearray(0), ExitProgMode_UPDI, 0)
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
            self.run_Script(self.script_cmd_type, bytearray(0), EnterDebugMode_UPDI, 0)
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
            self.run_Script(self.script_cmd_type, bytearray(0), ExitDebugMode_UPDI, 0)
            ret = self.read_response("Exit Debug Mode")[0]
            if (ret == 0x00):
                self._probeMode = probeMode.OFF
                print("INFO: Left DEBUG mode")
        else:
            print("ERROR: Can't leave DEBUG mode, Target not in DEBUG Mode")
        #EOF


    def halt_Target(self):
        self.run_Script(self.script_cmd_type, bytearray(0), Halt_UPDI, 0)
        ret = self.read_response("Halt Target")[0]
        if (ret == 0x00):
            self._targetState = targetState.HALT
            return True
        else:
            return False
        #EOF


    def resume_Target(self):
        self.run_Script(self.script_cmd_type, bytearray(0), Run_UPDI, 0)
        ret = self.read_response("Resume Target")[0]
        if (ret == 0x00):
            self._targetState = targetState.RUN
            return True
        else:
            return False
        #EOF


    def get_halt_status(self):  # Returns True if halted
        self.run_Script(self.script_cmd_type, bytearray(0), GetHaltStatus_UPDI, 0)
        ret = self.read_response("Halt Status")[1]
        self._target_halt_status = get_uint32_from_buf(ret, 0)
        if self._target_halt_status == 0xAAAAAAAA:
            return True
        else:
            return False
        #EOF


    def reset_Target(self): # Will halt automatically
        self.run_Script(self.script_cmd_type, bytearray(0), DebugReset_UPDI, 0)
        self.read_response("Reset Target")


    def reset_halt_Target(self):
        self.halt_Target()
        self.reset_Target()


    def set_hw_breakpoint(self, num:int, addr:int):
        param = uint32_to_buf(num)
        param += uint32_to_buf(addr)
        self.run_Script(self.script_cmd_type, param, SetHWBP_UPDI, 0)
        ret = self.read_response("Set HW breakpoint")[0]
        if ret != 0x00:
            print("ERROR: Failed setting HW breakpoint {0} at addr {1:04X}".format(num, addr))
            return False
        return True
        #EOF


    def clear_hw_breakpoint(self, num:int):
        param = uint32_to_buf(num)
        self.run_Script(self.script_cmd_type, param, ClearHWBP_UPDI, 0)
        ret = self.read_response("Set HW breakpoint")[0]
        if ret != 0x00:
            print("ERROR: Failed clearing HW breakpoint {0}".format(num))
            return False
        return True
        #EOF


    def step_target(self):
        self.run_Script(self.script_cmd_type, [], SingleStep_UPDI, 0)
        ret = self.read_response("Single Step")[0]
        if ret != 0x00:
            print("ERROR: Failed Stepping to next instruction")
            return False
        return True
        

    def get_PC(self):
        self.run_Script(self.script_cmd_type, bytearray(0), GetPC_UPDI, 0)
        ret = self.read_response("get_PC")[1]

        self.target_pc = get_uint32_from_buf(ret, 0)
        #print("Current PC: {0:06X}".format(self.target_pc))
        return ret   # get byte (LE) representation 
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

        if self._device_info == None:
            print("ERROR: Device must be known to Write PC to it")
            return
        
        flash_size = self._device_info[devlut_flash_len]
        flash_mask = (flash_size >> 9) - 1  # Max PC is half the Flash size
        param[3] = 0x00     # make sure to have valid inputs only
        param[2] = 0x00
        
        if (param[1] > flash_mask):
            print("ERROR: PC bigger then Flash Size")
            return
            
        self.run_Script(self.script_cmd_type, param, SetPC_UPDI, 0)
        ret = self.read_response("set_PC")[0]
        if ret == 0x00:
            return True
        else:
            return False
        #EOF


    def get_SP_SREG(self):
        return self.read_device_mem8(0x3D, 3)
        #EOF


    def get_device_ID(self, force:bool = False):

        if (self._devID == 0x00) or (force is True):
            self.run_Script(self.script_cmd_type, bytearray(0), GetDeviceID_UPDI, 0)
            ret = self.read_response("Get Device ID")[1]
            revision = ret[3]
            devID = ret[0] << 16 | ret[1] << 8 | ret[2]

            try:
                device_mem = device_lut[devID]
            except(KeyError, IndexError):
                print("Device not yet in the Lookup Table: {0:06X}".format(devID))
            
            if (device_mem != None):
                self._device_info       = device_mem
                self._devID             = devID
                self._revision          = revision
                print("Device ID: {0:06X}, Device Name: {1}".format(devID, device_mem[devlut_devname]))
        #EOF


    def check_BIST(self):
        key = b"BIST Tested"
        self.get_Status_From_String(key, "check BIST")

        key = b"BIST Results"
        self.get_Status_From_String(key, "check BIST")


    def get_Target_Id(self):
        self.enter_Prog_Mode()
        self.check_BIST()
        self.get_device_ID()
        self.exit_Prog_Mode()


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

        self._icd.write(self._cmd_write_ep, transfer)
        #EOF


    def read_response(self, func:str, timeout:int = 1000):
        ret = self._icd.read(self._cmd_read_ep, 1024, timeout)
        response_status = get_uint32_from_buf(ret, 0)
        if (response_status != 0x0D):
            raise ValueError("Wrong Device Response On '" + func + "'. Repose: {0}".format(ret))
        
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
        read_len = ((expected_len // 512) + 1) * 512
        ret = self._icd.read(self._data_read_ep, read_len, 1000)
        received_len = len(ret) 
        if (received_len!= expected_len):
            print('WARNING: Wrong Number of Received Bytes in "{0}". Expected: {1}. Received: {2}'.format(func, expected_len, received_len))
        
        return ret
        #EOF


    def write_script_download(self, data:bytearray, func:str):
        self._icd.write(self._data_write_ep, data)

  

    def send_script_done(self, func:str):
        script_done_type = 0x0103  # == 259
        transfer = self.create_msg_header(script_done_type, 16, 0)
        self._icd.write(self._cmd_write_ep, transfer)

        self.read_response(func)
        #EOF


    def get_Status_From_String(self, key:bytes, func:str):
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
        self._create_mem_map_xml()
        return self._memory_map_xml
        #EOF


    def get_target_xml(self):
        self._create_target_xml()
        return self._target_xml
        #EOF


    def get_threads_xml(self):
        tree_thread = ET.Element('threads')
        tread = ET.SubElement(tree_thread, 'thread', id="1", name="Main")
        head = b'<?xml version="1.0"?><!DOCTYPE feature SYSTEM "threads.dtd">'
        return head + ET.tostring(tree_thread)


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
        cpu_regs = self.read_device_mem8(0, 32) # limit to all CPU regs for now 
        sreg_sp = self.read_device_mem8(0x3D, 3)
        cpu_pc = self.get_PC()

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
        ret_val += self.conv_byte_to_hex(cpu_pc[0])
        ret_val += self.conv_byte_to_hex(cpu_pc[1])
        ret_val += self.conv_byte_to_hex(cpu_pc[2])
        ret_val += self.conv_byte_to_hex(cpu_pc[3])
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
        self.write_device_mem8(addr, data[0:32])    # CPU Regs, all in one go
        self.write_device_mem8(0x3F, data[32:33])   # SREG
        self.write_device_mem8(0x3D, data[33:35])   # SP
        self.set_PC(data[35:39])                    # PC


    def get_target_register(self, reg:int):
        if reg in range(0, 32):
            val &= 0xFF
            addr = 4000 + reg
            param = [val]
            self.write_device_mem8(addr, param)
        elif reg == 32:     # SREG
            val &= 0xFF
            addr = 0x3F
            param = [val]
            self.write_device_mem8(addr, param)
        elif reg == 33:     # SP
            addr = 0x3D
            param = [val & 0xFF, (val>>8) & 0xFF]
            self.write_device_mem8(addr, param)
        elif reg == 34:
            self.set_PC(val)
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
            ret_val = self.write_device_mem8(addr, param)
        elif reg == 32:     # SREG
            val &= 0xFF
            addr = 0x3F
            param = [val]
            ret_val = self.write_device_mem8(addr, param)
        elif reg == 33:     # SP
            addr = 0x3D
            param = [val & 0xFF, (val>>8) & 0xFF]
            ret_val = self.write_device_mem8(addr, param)
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
        
        param = uint32_to_buf(0x80000 + start_mod)
        param += uint32_to_buf(len_mod)

        self.run_Script(self.script_upload_type, param, ReadProgmem_UPDI, len_mod)
        self.read_response("Read Program Memory")
        ret = self.read_script_upload(len_mod, "Read Program Memory")
        self.send_script_done("Read Program Memory")

        ret = ret[start_modulo:(start_modulo+len)]
        return ret


    def prepare_target_flash(self, start:int, data:bytes):
        #if (self._targetState != targetState.ERASED):
        #    return False    # Abort, Target, not ready to be written to
        #self.enter_Debug_Mode()
        data_len = len(data)
        

        # Fill "empty" space with 0xFF
        #fill = 0xFF
        #fill = fill.to_bytes(1, 'little')
        for x in range (self._program_tail, start):
            self._new_program.append(255)
            self._program_tail += 1
        
        self._new_program += data
        self._program_tail += data_len
        #EOF


    def finalize_download(self):
        if (self.erase_target_flash() == False):
            return False
        
        self.enter_Prog_Mode()

        transfers = (self._program_tail // 512) + 1    # split to 512 byte long frames
        transfer_mod = self._program_tail % 512
        if (transfer_mod != 0):
            for x in range (transfer_mod, 512):    # Fill our new Program up to the next full 512
                self._new_program.append(255)
                self._program_tail += 1
        
        print("INFO: Starting Programming: Block count: {0}, Program Length: {1}". format(transfers, self._program_tail))

        param = uint32_to_buf(0x80000)
        param += uint32_to_buf(self._program_tail)

        # Start Programming
        self.run_Script(self.script_download_type, param, WriteProgmem_UPDI, self._program_tail)
        self.read_response("Download Program")

        # Program Flash
        self._icd.write(self._data_write_ep, self._new_program)
        
        # Check for Errors
        key = b"ERROR_STATUS_KEY"
        ret = self.get_Status_From_String(key, "Download Program")
        self.send_script_done("Download Program")
        if not (ret.startswith(b"NONE")):
            print ("ERROR: Download Program failed, code: {0}".format(ret)) 

        downloaded_code = self.read_target_flash(0x80000, self._program_tail)

        if (len(self._new_program) != len(downloaded_code)):
            print("WARNING: Different Code Sizes")
        else:
            failed = 0
            for x in range (0, len(self._new_program)):
                if (self._new_program[x] != downloaded_code[x]):
                    print("WARNING: PROGMEM discrepancy Found on pos {0}". format(x))
                    failed = 1
                    break
            if (failed == 0):
                print("INFO: Download Successful")
        
        self.target_flash_erased = 0
        self.exit_Prog_Mode()
        # Reset variables
        self._new_program = []
        self._program_tail = 0

        self.enter_Debug_Mode()

        pass

        #EOF


    def erase_target_flash(self):
        if (self.target_flash_erased == 1):
            return True
        self.enter_Prog_Mode()
        print("INFO: Erasing Target")
        self.run_Script(self.script_cmd_type, bytearray(0), EraseChip_UPDI, 0)
        ret = self.read_response("Erase Chip")[0]
        self.exit_Prog_Mode()
        if ret == 0x00:
            self.target_flash_erased = 1
            return True
        else:
            return False
        #EOF


    def read_device_mem8(self, addr:int, read_len:int):
        param = uint32_to_buf(addr)
        param += uint32_to_buf(read_len)
        self.run_Script(self.script_upload_type, param, ReadMem8_UPDI, read_len)    # reading only 1 byte

        self.read_response("Read Device Mem8")
        ret = self.read_script_upload(read_len, "Read Device Mem8")   

        self.send_script_done("Read Device Mem8")
        return ret
        #EOF
    

    def write_device_mem8(self, addr:int, value:bytearray):
        if (self._probeMode != probeMode.DEBUG):
            print("ERROR: Attempt to write register memory outside Debug Mode")
            return False
        
        write_len = len(value)
        param = uint32_to_buf(addr)
        param += uint32_to_buf(write_len)

        self.run_Script(self.script_download_type, param, WriteMem8_UPDI, write_len)
        ret = self.read_response("Write Device Mem8")[0]
        if (ret != 0x00):
            print ("ERROR: Init Write Mem8 failed, code: {0}".format(ret))
            return False
        
        self._icd.write(self._data_write_ep, value)  # write new value to memory

        key = b"ERROR_STATUS_KEY"

        ret = self.get_Status_From_String(key, "Write Device Mem8")
        self.send_script_done("Write Device Mem8")
        if not (ret.startswith(b"NONE")):
            print ("ERROR: Download Program failed, code: {0}".format(ret)) 
            return False
        
        return True
        #EOF


#    def enter_downloading_mode(self):
#        if (self._probeMode == probeMode.DEBUG):
#            self.exit_Debug_mode()
#
#        if (self.erase_target_flash() == True):
#            self._targetState = targetState.ERASED
#            return True
#
        #return False
        #EOF


    def attach_power(self):
        self.get_Voltages()                             # 0x47
        if (self.VddVoltageSense < 1000):  # Only power the system if there is no voltage already
            if (self._voltage >= 1800):
                self.select_power_source(True)          # 0x46
                self.disable_Power_System()             # 0x44
                self.enable_Power_System(self._voltage) # 0x40  ToDo: Figure out live connect with disabled power supply
            else:
                self.select_power_source(False)         # 0x46
                self.disable_Power_System()             # 0x44
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
        self._target_attached = True
        #EOF


    def detach_target(self):
        if (self._probeMode == probeMode.DEBUG):
            self.exit_Debug_Mode()          # len 0x1A
        elif (self._probeMode == probeMode.PROG):
            self.exit_Prog_Mode()
        self._targetState = targetState.OFF
        self.set_live_connect(False)        # 0x39
        self.disable_Power_System()         # 0x44
        self._target_attached = False       # Always allow detatching


    def refresh_icd_status(self):
        self.get_Firmware_Info()                # 0xE1
        self.set_PTG_mode(False)                # 0x5E; 0x00
        self.set_live_connect(False)            # 0x39
        self.attach_power()
        self.set_LED_Brightness(5)              # 0xCF
        self.set_UPDI_Speed(self._updi_speed)   # 0x91
        self.get_Target_Id()
        self.set_live_connect(False)
        self.disable_Power_System()
        #EOF


    def live_connect_to_device(self):
        self.get_Firmware_Info()                    # 0xE1
        self.set_PTG_mode(False)                    # 0x5E; 0x00
        
        self.set_live_connect(True)                # 0x39

        if (self._voltage >= 1800):
            self.select_power_source(True)          # 0x46
            self.disable_Power_System()             # 0x44
            self.enable_Power_System(self._voltage) # 0x40  ToDo: Figure out live connect with disabled power supply
        else:
            self.select_power_source(False)         # 0x46
            self.disable_Power_System()             # 0x44

        self.get_Voltages()                     # 0x47
        self.set_LED_Brightness(5)              # 0xCF
        self.set_UPDI_Speed(self._updi_speed)   # len 0x21
        self.get_Target_Id()
        self.enter_Debug_Mode()                 # len 0x6C
        self.halt_Target()                      # len 0x59
        self.get_halt_status()                  # len 0x59; 0x45
        self.get_PC()                           # len 0x3D
        self.read_device_mem8(0x3F, 1)          # len 0x33; 0x3F
        #EOF


    def reset_connected_device(self):
        self.reset_Target()                 # len 0x53
        self.get_PC()                       # len 0x3D
        self.read_device_mem8(0x3F)         # len 0x33
        #EOF


    def disconnect_from_target(self):
        self.exit_Debug_Mode()          # len 0x1A
        #self.get_Firmware_Info()        # 0xE1
        self.set_live_connect(True)     # 0x39
        self.disable_Power_System()     # 0x44
#EOC
