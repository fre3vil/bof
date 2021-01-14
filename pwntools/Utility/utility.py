#!/usr/bin/env python3



from pwn import *


'''
# version 1

import struct

def p(x):
    return struct.pack('I', x)

def u(x):
    return struct.unpack('I', x)[0]

print(p(1234))
print(u(p(1234)))
print(1234 == u(p(1234)))

'''


print(pack(1234))
print(unpack(pack(1234)))
print(1234 == unpack(pack(1234)))
