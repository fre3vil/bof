### The basic

```
$ objdump -D -M intel hello_world
$ objdump -M intel -D hello_world | grep '[0-9a-f]:' | grep -v 'file' | cut -f2 -d: | cut -f1-7 -d' ' | tr -s ' ' | tr '\t' ' ' | sed 's/ $//g' | sed 's/ /\\\x/g' | paste -d '' -s 
$ gcc -fno-stack-protector -z execstack -o shellcode_helllworld shellcode_helllworld.c
```

### bad character
```
00 => \0
0A => \n
FF => \f
0D => \r
```


### xor_helloworld.nasm
```
$ nasm -felf64 xor_helloworld.nasm -o xor_helloworld.o
$ ld xor_helloworld.o -o xor_helloworld
$ objdump -D -M intel xor_helloworld
```

### jmp
```
$ nasm -felf64 jmp.nasm -o jmp.o
$ ld jmp.o -o jmp
$ objdump -M intel -D jmp
```
