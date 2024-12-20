# Square.py


import math

def is_square(n):
    # take the square root
    root = math.sqrt(n)
    if root == int(root):
        return True
    else:
        return False

for x in range(0,17):
    print(x, is_square(x))
