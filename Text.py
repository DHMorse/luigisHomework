# Text.py

from tkinter import *
root = Tk()

canvas = Canvas(root, width=600, height=450, bg="#000000")
canvas.pack()

canvas.create_line(200, 0, 200, 450, fill="#404040")
canvas.create_line(0, 200, 600, 200, fill="#404040")
canvas.create_text(200, 200, text="Message for you, sir.",
                   fill="#FFA000",
                   font=("Comic Sans MS",18))
