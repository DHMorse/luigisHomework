# Dice_Rolling.py

import random

def roll_one_die():
    n = random.randint(1, 6)
    return n

def roll_two_dice():
    #n1 = random.randint(1, 6)
    #n2 = random.randint(1, 6)
    #n = n1 + n2
    # return n
    # Cleaner one line version
    return random.randint(1, 6) + random.randint(1, 6)

def display_die(n):
    if n == 1:
        print(" ------- ")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print(" ------- ")
    elif n == 2:
        print(" ------- ")
        print("| o     |")
        print("|       |")
        print("|     o |")
        print(" ------- ")
    elif n == 3:
        print(" ------- ")
        print("| o     |")
        print("|   o   |")
        print("|     o |")
        print(" ------- ")
    elif n == 4:
        print(" ------- ")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print(" ------- ")
    elif n == 5:
        print(" ------- ")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print(" ------- ")
    elif n == 6:
        print(" ------- ")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print(" ------- ")

def roll_many(n, display):
    total = 0
    i = 0
    while (i < n):
        number = random.randint(1, 6)
        if display == True:
            display_die(number)
        total = total + number
        i = i + 1
    return total
