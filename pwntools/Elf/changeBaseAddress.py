#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")



e = ELF("/bin/bash")
print("%#x -> base address" % e.address)
print("%#x -> entry point" % e.entry)
print("%#x -> execve" % e.symbols['execve'])

print("change base address now!!!!")
e.address = 0x12340000
print("%#x -> base address" % e.address)
print("%#x -> entry point" % e.entry)
print("%#x -> execve" % e.symbols['execve'])


