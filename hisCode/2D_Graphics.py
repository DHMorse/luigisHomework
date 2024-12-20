# 2D_Graphics

from tkinter import *

c = Canvas(width=400, height=300, bg="Black")

c.create_rectangle(50, 50, 100, 100, outline="Red", width=2,
                   fill="Yellow",activefill="Blue",
                   dash=(20, 10),stipple="info")

c.pack()
mainloop()
