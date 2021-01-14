#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")



e = ELF("/bin/bash")

print(repr(e.read(e.address, 4)))

p_license = e.symbols['bash_license']
license = e.unpack(p_license)
print("%#x -> %#x" % (p_license, license))
print(e.read(license, 4))
print(e.disasm(e.symbols['main'], 12))
