#!/usr/bin/env python3




from pwn import *

host = "223.5.5.5"
port = 53
proto = "udp"

dns = remote(host, port, type=proto)
tcp6 = remote('google.com', 80, fam='ipv6')


