# Screen Coordinates.py

from tkinter import *

c = Canvas(width=600, height=450, bg="Black")

x = 100
y = 100

c.create_rectangle(x, y, x+200, y+300,
                    outline="Yellow",width=2)

c.create_line(x, y+150, x+200, y+150,
              fill="Yellow",width=2)
c.create_line(x+100, y, x+100, y+300,
              fill="Yellow",width=2)

c.pack()
c.mainloop()