global _start

section .text

_start:
    mov rax, 0x1234
    mov rbx, 0x5678

    mov rdi, rax
    mov rsi, rbx

    mov rax, 60
    mov rdi, 0
    syscall

section .data
