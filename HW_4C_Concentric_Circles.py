# HW_4C_Concentric_Circles
# Luke Norvell

from tkinter import *
from random import randint

def get_color():
    color = randint(1,3)
    if color == 1:
        color = 'Green'
    elif color == 2:
        color = 'Blue'
    elif color == 3:
        color = 'White'
    return color

c = Canvas(width=800, height=600, bg="Black")

for i in range (1,31):
    c.create_arc(400 - i*5, 300 - i*5, 400 + i*5, 300 + i*5, extent=359.9,width=2, style=CHORD, 
    outline=get_color())
    print("Circle "+ str(i) + " has been made!") # This is just to make sure 30 circles have in fact been made
    
    # I'm not sure if this was the solution to the answer... it's either this or the same thing but the fill is the random color. In that case this code is used:
    # c.create_arc(400 - i*5, 300 - i*5, 400 + i*5, 300 + i*5, extent=359.9,width=2, style=CHORD, fill=get_color())


c.pack()
c.mainloop()