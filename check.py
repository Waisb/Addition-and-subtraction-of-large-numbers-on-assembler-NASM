import sys
import os
if (len(sys.argv) < 4):
    print("Usage:\npython check.py [NUM1] [ACTION] [NUM2]\nAction list:\n+ addition\n- subtraction")
    exit(0)

num1_name = sys.argv[1]
num2_name = sys.argv[3]
action = sys.argv[2]

def compilation(num1_name = num1_name, num2_name = num2_name, action = action):
    os.system(f"nasm -felf64 prog.asm && ld prog.o && ./a.out {num1_name} {num2_name} {action}")

def addition(num1_name = num1_name, num2_name = num2_name):
    num1 = open(num1_name, 'rb');
    num2 = open(num2_name, 'rb');
    output = open("output", 'rb');
    num1 = num1.read();
    num2 = num2.read();
    output = output.read();
    num1 = int.from_bytes(num1, 'little');
    num2 = int.from_bytes(num2, 'little');
    output = int.from_bytes(output, 'little');
    print("num1 = ",hex(num1));
    print("num2 = ", hex(num2));
    print("num1 + num2 = ", hex(num1+num2));
    print("output = " , hex(output));
    if (num1+num2 == output):
        print("Получилось");
    else:
        print("Не получилось");

def subtraction(num1_name = num1_name, num2_name = num2_name):
    num1 = open(num1_name, 'rb');
    num2 = open(num2_name, 'rb');
    output = open("output", 'rb');
    num1 = num1.read();
    num2 = num2.read();
    output = output.read();
    num1 = int.from_bytes(num1, 'little');
    num2 = int.from_bytes(num2, 'little');
    output = int.from_bytes(output, 'little');
    print("num1 = ",hex(num1));
    print("num2 = ", hex(num2));
    print("num1 - num2 = ", hex((num1-num2) & (2**256-1)));
    print("output =      " , hex(output));
    if ((hex((num1-num2) & (2**256-1))) == hex(output)):
        print("Получилось")
    else:
        print("Не получилось")    

def multiplication(num1_name = num1_name, num2_name = num2_name):
    num1 = open(num1_name, 'rb');
    num2 = open(num2_name, 'rb');
    output = open("output", 'rb')
    num1 = num1.read()
    num2 = num2.read()
    output = output.read()
    num1 = int.from_bytes(num1, 'little')
    num2 = int.from_bytes(num2, 'little')
    output = int.from_bytes(output, 'little')
    print ("num1 = ", hex(num1))
    print ("num2 = ", hex(num2))
    #print ("num1 * num2 = ", hex((num1*num2) & (2**256-1)))
    print ("num1 * num2 = ", hex(num1*num2))
    print ("output =      ", hex(output))
    #print ("output =      ", hex((output)&(2**256-1)))

def shift_left(num1_name = num1_name, num2_name = num2_name):
    num1 = open(num1_name, 'rb');
    num2 = open(num2_name, 'rb');
    output = open("output", 'rb')
    num1 = num1.read()
    num2 = num2.read()
    output = output.read()
    num1 = int.from_bytes(num1, 'little')
    num2 = int.from_bytes(num2, 'little')
    output = int.from_bytes(output, 'little')
    print ("num1          ", hex(num1))
    print ("num2          ", hex(num2))
    #print ("num1<<num2      ", hex(num1<<num2))
    print ("output =      ", hex(output))



#Компиляция при любых переданных параметрах
compilation()



if (action == '+'):
    addition()
if (action == '-'):
    subtraction()
if (action == '='): #fixthat later
    multiplication()
if (action == 'l'):
    shift_left()
