; NASM amd64 Linuc

section .data
	msg db "Иди нахуй", 10
	msglen equ $ - msg

section .text
	global _start

_start:
	mov rax, 1
	mov rdi, 1
	mov rsi, msg
	mov rdx, msglen
	syscall

	mov rax, 60
	xor rdi, rdi
	syscall
