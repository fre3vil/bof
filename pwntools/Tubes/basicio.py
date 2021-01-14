#!/usr/bin/env python3




from pwn import *
io = process('sh')
io.sendline('echo hello world.')
print(io.recvline())



