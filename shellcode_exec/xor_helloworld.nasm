global _start

section .text

_start:
    
    mov al, 1
    xor rdi, rdi
    mov rdi, 1
    mov rsi, hello_world
    xor rdx, rdx
    add rdx, 12
    syscall

    xor rax, rax
    add rax, 60
    xor rdi, rdi
    syscall

section .data
    
    hello_world: db 'hello_world', 0xa
