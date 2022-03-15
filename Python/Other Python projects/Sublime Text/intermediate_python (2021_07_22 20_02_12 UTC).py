# import os

# who = "Gary"
# how_many = 12

# print(f'{who} bought {how_many} apples today!')

# import argparse
# import sys
def calculation(x, y, operation):
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y
    elif operation == 'remainder':
        return x // y
    elif operation == 'exponent':
        return x ** y

x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
operation = input("What operation to perform? add, sub, mul, div, remainder, exponent:")

# inp = input_numbers(global_i = True)
calc = calculation(x, y, operation)
print(calc)
