#!/usr/bin/env python3




from pwn import *


client = listen(8080).wait_for_connection()


