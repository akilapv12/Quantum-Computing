# A Simple Calculator
x=float(input("Enter first number: "))
y=float(input("Enter second number: "))
z=input("Enter operation (+, -, *, /, %, **, //): ")
if z == "+":
    print("Result:", x + y)
elif z == "-":
    print("Result:", x - y)
elif z == "*":
    print("Result:", x * y)
elif z == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Result: Division by zero error")
elif z == "%":
    if y != 0:
        print("Result:", x % y)
    else:
        print("Result: Division by zero error")
elif z == "**":
    print("Result:", x ** y)
elif z == "//":
    if y != 0:
        print("Result:", x // y)
    else:
        print("Result: Division by zero error")
else:
    print("Invalid operation")