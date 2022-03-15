import math

maths = math


class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self, x, y):
        self.x = x
        self.y = y
        z = x + y
        return z
    def sub(self,x, y):
        self.x = x
        self.y = y
        return x - y


a = int(input("What's the first number?"))
b = int(input("What's the Second number?"))
ad = Calculator(a, b)
ad.add(a, b)
print(ad)



