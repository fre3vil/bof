#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")



e = ELF('/bin/bash')

for address in e.search('/bin/sh\x00'.encode()):
    print(hex(address))
