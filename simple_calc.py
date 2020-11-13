"""This is a simple calculator. It will at the very least, add, subtract,
multiply, and divide. I may at some later point, add more complicated math
functions, but this basic implementation will just so some simple math."""

def add(a,b):
    """This function will add two numbers, a b, together"""
    return a+b

def subtract(a,b):
    """This function subtracts b from a"""
    return a-b

def multiply(a,b):
    """This function multiplies a by b"""
    return a*b

def divide(a,b):
    """This function divides a by b"""
    return a/b
result = None
while True:
    print("Hello, what math can I do for you today?")
    selection = input("""What math function should I run,
    Or should I clear the previous result first?""")
    if selection == "end":
        break
    if selection == "clear":
        result = None
        continue
    num1 = int(input("What's the first number I should use?"))
    if result == None:
        num2 = int(input("What's the second number I should use?"))

    if selection == "add" and result == None:
        result = add(num1, num2)
        print(result)
    elif selection == "add" and result is not None:
        result = add(result, num1)
        print(result)
    if selection == "subtract" and result == None:
        result = subtract(num1, num2)
        print(result)
    elif selection == "subtract" and result is not None:
        result = subtract(result, num1)
        print(result)
    if selection == "multiply" and result == None:
        result = multiply(num1, num2)
        print(result)
    elif selection == "multiply" and result is not None:
        result = multiply(result, num1)
        print(result)
    if selection == "divide" and result == None:
        result = divide(num1, num2)
        print(result)
    elif selection == "divide" and result is not None:
        result = divide(result, num1)
        print(result)
    
        