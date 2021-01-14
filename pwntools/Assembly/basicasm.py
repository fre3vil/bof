#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")



print(repr(asm('xor edi, edi')))
print(enhex(asm('xor edi, edi')))
