# Event_Binding.py

from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=400)
canvas.pack()

thing1 = canvas.create_rectangle(10, 50, 20, 60, outline="#0000AA", width=2)

def move(event):
    if event.keysym == "Left":
        canvas.move(thing1, -10, 0)
    elif event.keysym == "Right":
        canvas.move(thing1, 10, 0)
    elif event.keysym == "Up":
        canvas.move(thing1, 0, -10)
    elif event.keysym == "Down":
        canvas.move(thing1, 0, 10)

canvas.bind_all("<KeyPress-Left>", move)
canvas.bind_all("<KeyPress-Right>", move)
canvas.bind_all("<KeyPress-Up>", move)
canvas.bind_all("<KeyPress-Down>", move)

mainloop()
