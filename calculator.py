"""
Simple Calculator Program.
Supports addition, subtraction, multiplication and division.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Cannot divide by 0.")
    return a / b

# print("Calculator Program")
# print("Addition:", add(10, 5))

if __name__ == "__main__":
    x = float(input("Enter x: "))
    y = float(input("Enter y: "))
    print("Addition:", add(x, y))
    print("Subtraction:", subtract(x, y))
    print("Multiplication:", multiply(x, y))
    print("Division:", divide(x, y))

    print("Thank you for using the calculator!")