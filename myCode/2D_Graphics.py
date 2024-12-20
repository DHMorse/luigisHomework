# 2D_Graphics

from tkinter import *

myCanvas: Canvas = Canvas(width=400, height=300, bg="Black")

myCanvas.create_rectangle(50, 50, 100, 100, outline="Red", width=2,
                    fill="Yellow",activefill="Blue",
                    dash=(20, 10),stipple="info")

if __name__ == '__main__':
    myCanvas.pack()
    mainloop()
