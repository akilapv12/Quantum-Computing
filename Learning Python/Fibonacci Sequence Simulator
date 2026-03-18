# Fibonacci Sequence Simulatar:
# The Fibonacci sequence is a famous number pattern where each number is the sum of the two numbers before it.

a = input("Enter 1st number in the patter: ")
b = input("Enter 2nd number in the patter: ")
r = input("Enter the number of numbers you want in the pattern: ")
try:
    a = int(a)
    b = int(b)
    r = int(r)
    for i in range(r+1):
        a, b = b, a+b
        print(a)
except ValueError:
    print("All 1st number, 2nd number, and range of numbers should be integers.")