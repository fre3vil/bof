#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")




ELF.from_bytes('\xcc'.encode()).save('int3-1')
ELF.from_assembly('int3').save('int3-2')
ELF.from_assembly('nop', arch='amd64').save('amd64-nop')
