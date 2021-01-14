#!/usr/bin/env python3




from pwn import *

host = "192.168.2.84"
port = 8888
data = "GET /\r\n\r\n"

io = remote(host, port)
io.send(data)
print(io.recvline())

