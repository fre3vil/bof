#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# fuzz for vulnserver

import sys
from time import sleep
import socket

initSize = int(sys.argv[3])

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
        sleep(1)
        socks.close()

if __name__ == '__main__':

    # buffer create python -c 'print("A"*100)'
    buff = "A" * initSize
    host = str(sys.argv[1])
    port = int(sys.argv[2])
    
    for i in range(20):
        buff = buff * i
        attack(host, port, buff)
