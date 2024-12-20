# Direction.py

from tkinter import *
root = Tk()
c = Canvas(root, width=1000, height=1000)

rect = c.create_rectangle(50, 50, 60, 60, width=2, outline="#880000")
c.pack()

direction = "none"
xvel = 0
yvel = 0

def move_rectangle():
    c.move(rect, xvel, yvel)
    c.after(20, move_rectangle)

def change_speed(event):
    global direction
    global xvel
    global yvel
    if event.keysym == "Left":
        xvel = xvel - 0.4
    elif event.keysym == "Right":
        xvel = xvel + 0.4
    elif event.keysym == "Up":
        yvel = yvel - 0.4
    elif event.keysym == "Down":
        yvel = yvel + 0.4
    elif event.keysym == "s":
        xvel = 0
        yvel = 0

c.bind_all("<KeyPress-Left>", change_speed)
c.bind_all("<KeyPress-Right>", change_speed)
c.bind_all("<KeyPress-Up>", change_speed)
c.bind_all("<KeyPress-Down>", change_speed)
c.bind_all("<KeyPress-s>", change_speed)

move_rectangle()
mainloop()