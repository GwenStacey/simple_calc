"""This is a simple calculator. It will at the very least, add, subtract,
multiply, and divide. I may at some later point, add more complicated math
functions, but this basic implementation will just so some simple math."""

def add(a,b):
    """This function will add two numbers, a b, together"""
    return a+b

def subtract(a,b):
    return a-b

while True:
    print("Hello, what math can I do for you today?")
    selection = input("What math function should I run?")
    if selection == "end":
        break
    num1 = int(input("What's the first number I should use?"))
    num2 = int(input("What's the second number I should use?"))
    if selection == "add":
        print(add(num1, num2))
    if selection =="subtract":
        print(subtract(num1, num2))
    
        