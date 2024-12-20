# Simple_Animation.py

from tkinter import *
from time import *

root = Tk()
canvas = Canvas(root, width=600, height=400)
canvas.pack()

thing1 = canvas.create_rectangle(10, 50, 20, 60, outline="#0000AA", width=2)

thing2 = canvas.create_arc(10, 300, 20, 310, outline="#AA0000",
                           width=2,extent=359.9, style=ARC)

for i in range (0, 200):
    canvas.move(thing1, 1, 0.2)
    canvas.move(thing2, 0.8, -1.5)
    root.update()
    sleep(0.02)
