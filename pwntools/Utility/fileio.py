#!/usr/bin/env python3



from pwn import *
wfile = 'w.txt'
data = 'using pwntools write file.'

write(wfile, data)
print(read(wfile))
print(read(wfile, 1))
