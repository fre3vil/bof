#!/usr/bin/env python3




from pwn import *


io = serialtube('/dev/ttyUSB0', baudrate=115200)


