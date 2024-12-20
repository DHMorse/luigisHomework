# HW_4B_Screen_Coordinates
# Luke Norvell

from tkinter import *

c = Canvas(width=800, height=600, bg="Black")

# Probably could've been done easier by making the computer doing the math, but oh well 
c.create_rectangle(200, 150, 600, 450, outline="Blue", width=1)
c.create_rectangle(225, 175, 575, 425, outline="Blue", width=1)
c.create_line(200, 150, 225, 175, fill="Blue")
c.create_line(600, 150, 575, 175, fill="Blue")
c.create_line(200, 450, 225, 425, fill="Blue")
c.create_line(600, 450, 575, 425, fill="Blue")


c.pack()
c.mainloop()