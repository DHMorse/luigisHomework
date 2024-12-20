# Paint.py
w = float(input("width? "))
h = float(input("height? "))

area = w * h

import math
n = math.ceil(area / 250)
print("You need", n, "cans of paint")
