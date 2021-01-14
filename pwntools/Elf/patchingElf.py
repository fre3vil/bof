#!/usr/bin/env python3



from pwn import *

context(os="linux", arch="amd64", endian="little")



'''
$ chmod +x ./bash-modified
$ ./bash-modified -c 'exit'
Trace/breakpoint trap (core dumped)
$ ./bash-modified --version | grep "Hello"
Hello, world!
$ ./bash-modified -c 'cd "No chdir for you!"'
/home/user/No chdir for you!
No chdir for you!
./bash-modified: line 0: cd: No chdir for you!: No such file or directory

'''


e = ELF('/bin/bash')


# Cause a debug break on the 'exit' command
e.asm(e.symbols['exit_builtin'], 'int3')

# Disable chdir and just print it out instead
e.pack(e.got['chdir'], e.plt['puts'])

# Change the license
p_license = e.symbols['bash_license']
license = e.unpack(p_license)
e.write(license, 'Hello, world!\n\x00'.encode())

e.save('./bash-modified')


