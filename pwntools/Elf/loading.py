#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")

e = ELF("/bin/bash")

print("%#x -> licence" % e.symbols['bash_license'])
print("%#x -> execve" % e.symbols['execve'])
print("%#x -> got.execve" % e.got['execve'])
print("%#x -> plt.execve" % e.plt['execve'])
print("%#x -> list_all_jobs" % e.functions['list_all_jobs'].address)
