#!/usr/bin/env python3



from pwn import *

# base64

hstr = b"hello"
print(hstr)
print(b64e(hstr))
print(b64d(b64e(hstr)))


# Hashes
print(md5sumhex('hello'.encode()))
print(md5sumhex('hello'.encode()) == '5d41402abc4b2a76b9719d911017c592')

write('file.txt', 'hello')
print(md5filehex('file.txt'.encode()))
print(md5filehex('file.txt'.encode()) == '5d41402abc4b2a76b9719d911017c592')

print(sha1sumhex('hello'.encode()))
print(sha1sumhex('hello'.encode()) == 'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d')

# url encoding
print(urlencode("Hello, World!"))
print(urlencode("Hello, World!") == '%48%65%6c%6c%6f%2c%20%57%6f%72%6c%64%21')


# hex encode
print(b'hello') # byte format not use string
print("enhex('hello') = {}".format(enhex('hello'.encode())) )
print(unhex(enhex('hello'.encode())))


# Bit Manipulation and Hex Dumping

print("bits(0b1000001) = {result}".format(result = bits(0b1000001) )   )
print("bits('A') = {}".format( bits('A'.encode()) )  )
print(bits(0b1000001) == bits('A'.encode()))

# hex dumping
print(hexdump(read('/dev/urandom', 64)))


