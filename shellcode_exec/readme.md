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

#### mov_instruction
```
nasm -felf64 mov_instruction.nasm -o mov_instruction.o
ld mov_instruction.o -o mov_instruction64
```

#### control_flow
```
$ nasm -felf64 control_flow.nasm -o control_flow.o
$ ld control_flow.o -o control_flow

```

#### set_carry_flag
set carry flag (CF) can use stc 
```
$ nasm -felf64 set_carry_flag.nasm -o set_carry_flag.o
$ ld set_carry_flag.o -o set_carry_flag

```
#### set_zero_flag
```
$ nasm -felf64 set_zero_flag.nasm -o set_zero_flag.o
$ ld set_zero_flag.o -o set_zero_flag
```
