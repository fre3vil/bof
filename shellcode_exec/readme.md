# Penetration_testing_with_shellcode

#### linux64 hello world asm code

```
$ nasm -felf64 hello_world.nasm -o hello_world.o
$ ld hello_world.o -o hello_world
```


#### linux64 hello world stack asm code

```
$ nasm -felf64 hello_world_stack.nasm -o hello_world_stack.o
$ ld hello_world_stack.o -o hello_world_stack
```
