# Addition-and-subtraction-of-large-numbers-on-assembler-NASM
Сложение и вычитание чисел больших чем размер регистров

Числа находятся в файлах (в случае репрезитория в num1 и num2) и передаются в программу через аргументы
Так же есть проверка написанная на питоне, параметры передаются в виде [1число] [действие] [второе число]
Компилировать: nasm -felf64 prog.asm && ld prog.o
