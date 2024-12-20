# Tick.py

from tkinter import *
root = Tk()
c = Canvas(root, width=600, height=400)

def tick():
    print("I'd like to buy some cheese.")
    c.after(1000, tick)

c.after(3000, tick)
