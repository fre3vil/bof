global _start

section .text

_start:
    mov al, 0x1
    sub al, 0x3

jns exit
    mov rax, 1
    mov rax, 60
    mov rdi, 0
    syscall

exit:
    mov rax, 60
    mov rdi, 10
    syscall

section .data
