# Polgygon

from tkinter import *
root = Tk()
canvas = Canvas(root, width=400, height=300, bg="Black")
canvas.pack()

canvas.create_arc(140, 90, 160, 110, extent=359.9,
                  width=6, outline="Gray", style=ARC)

canvas.create_arc(240, 90, 260, 110, extent=359.9,
                  width=6, outline="Gray", style=ARC)
canvas.create_polygon(120, 100, 132, 100, 140, 87,
                      160, 87, 168, 100, 232, 100,
                      240, 87, 260, 87, 268, 100,
                      277, 100, 268, 80, 220, 75,
                      200,60, 160, 60, 135, 75,
                      outline="Blue",width=2)

canvas.create_polygon(138, 76, 217, 76,
                      197, 62, 162, 62,
                      outline="Gray",width=1)
root.mainloop()