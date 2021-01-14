#!/usr/bin/env python3




from pwn import *
io = process(['sh', '-c', 'echo A; sleep 1; echo B; sleep 1; echo C; sleep 1; echo DDDD'])
print(io.recv())
print(io.recvn(4))
print(hex(io.unpack()))


