# Hypotenuse.py

import math

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

a = 3
b = 4
print(a, b, hypotenuse(a, b))

a = 7
b = 24
print(a, b, hypotenuse(a, b))

a = 6.5
b = 8.3
print(a, b, hypotenuse(a, b))

