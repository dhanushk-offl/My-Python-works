#Simple Scientific Calculator
#Coded by: Dhanush
import math

def scientific_calc():
    print("Scientific Calculator")
    while True:
        op = input("Choose an operation (+, -, *, /, sin, cos, tan) or 'q' to quit: ")
        if op == 'q':
            break
        try:
            num = float(input("Enter a number: "))
            if op == '+':
                num2 = float(input("Enter another number: "))
                print(num + num2)
            elif op == '-':
                num2 = float(input("Enter another number: "))
                print(num - num2)
            elif op == '*':
                num2 = float(input("Enter another number: "))
                print(num * num2)
            elif op == '/':
                num2 = float(input("Enter another number: "))
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print(num / num2)
            elif op == 'sin':
                print(math.sin(num))
            elif op == 'cos':
                print(math.cos(num))
            elif op == 'tan':
                print(math.tan(num))
            else:
                print("Invalid operation")
        except ValueError:
            print("Invalid input")
