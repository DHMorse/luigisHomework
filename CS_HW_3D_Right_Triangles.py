# CS_HW_3D_Right_Triangles
# Luke Norvell

def is_right(len1, len2, len3):
    if len1 >= len2 and len1 >= len3:
        c = len1
        a = len2
        b = len3
    elif len2 >= len1 and len2 >= len3:
        c = len2
        a = len1
        b = len3
    else:
        c = len3
        a = len1
        b = len2

    if (a**2 + b**2) == (c**2):
        print("Triangle is a Right Triangle!")
    else:
        print("Triangle is not a Right Triangle.")


print("Enter three lengths of a triangle")
len1 = float(input("Length 1: "))
len2 = float(input("Length 2: "))
len3 = float(input("Length 3: "))
is_right(len1, len2, len3)