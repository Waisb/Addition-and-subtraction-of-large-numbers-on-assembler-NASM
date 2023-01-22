
;FILENAMES
section .data
      output db "output", 0       ;output
section .bss
	var_len equ 32
    ;sizing file descriptors 
    fd_num1 resb 4
    fd_num2 resb 4
    fd_output resb 4
    ;sizing vars from files
    var_num1 resb var_len
    var_num2 resb var_len
    var_output resb var_len

;Program start
section .text
    global _start
_start:
;Получение названий файлов и их дескрипторов через параметры.
;Справка:
;syscall принимает 8 байт в отличии от прерывания int 0x80. Потому для передачи параметров (которые 8 байт) использовать только syscall иначе прерыванием будет передаваться не правильно.
;NUM1 get fd
	mov rax,2
	mov rdi, [rsp+16]
	mov rsi,0
	mov rdx,0
	syscall
	mov [fd_num1], rax
;Num2 get fd
	mov rax, 2
	mov rdi, [rsp+24]
	mov rsi, 0
	mov rdx, 0
	syscall
	mov [fd_num2], rax
;NUM1 to var
    mov rax, 3
    mov rbx, [fd_num1]
    mov rcx, var_num1
    mov rdx, var_len
    int 0x80
;NUM2 to var
    mov rax, 3
    mov rbx, [fd_num2]
    mov rcx, var_num2
    mov rdx, var_len
    int 0x80


;Выбор действия
	mov rax, [rsp+32]
	cmp byte  [rax], '+'
	je addition_call
	cmp byte [rax], '-'
	je subtraction_call


addition_call:
    call addition
    jmp _end
subtraction_call:
    call subtraction
    jmp _end

;Вычитание
subtraction:
    xor rcx, rcx
    clc
    pushf
    mov rsi, var_num1
    mov rdi, var_output
    loop_check_subtraction:
    cmp rcx, var_len
    je loop_end_subtraction
    lodsq
    popf
    sbb rax, [var_num2+rcx]
    pushf
    stosq
    add rcx, 8
    jmp loop_check_subtraction
    loop_end_subtraction:
    popf
    ret
;Сложение
addition:   
	    xor rcx, rcx
	    clc	                    ;wipe carry flag
	    pushf	                ;safe carry flag
	    mov rsi, var_num1 	    ;use rsi to safe start of first string
	    mov rdi, var_output	    ;use rdi to safe start of output string
        loop_check_addition:
	    cmp rcx, var_len
	    je loop_end_addition
	    lodsq                   ;8 bites to RAX from rsi
	    popf                    ;get cary flags from stack
	    adc rax, [var_num2+rcx] 
	    pushf	                ;add cary flags to stack
	    stosq	                ;write rax to rsi +8 offset
	    add rcx, 8
	    jmp loop_check_addition
        loop_end_addition:
	    popf
        ret


;Запись в файл, закрытие всех файлов и окончание программы
_end:
;create the output file
    mov rax, 8
    mov rbx, output
    mov rcx, 420
    int 0x80
    mov [fd_output], rax
;write to output file
    mov rax, 4
    mov rbx, [fd_output]
    mov rcx, var_output
    mov rdx, var_len
    int 0x80
;close output file
    mov rax, 6
    mov rbx, [fd_output]
    int 0x80
;close other files
    mov rax, 6
    mov rbx, [fd_num1]
    int 0x80
    mov rax, 6
    mov rbx, [fd_num2]
    int 0x80
;program exit
    mov rax, 1
    mov rbx, 0
    int 0x80

