#!/usr/bin/env python3




from pwn import *

session = ssh('kali', '192.168.2.60', password='kali')

io = session.process('sh', env={"PS1":""})
io.sendline('echo hello world.')
print(io.recvline())



