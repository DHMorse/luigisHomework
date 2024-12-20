# Image.py

from tkinter import *
root = Tk()
canvas = Canvas(root, width=800, height=600, bg="#808080")
canvas.pack()

# Create a PhotoImage object
imgA = PhotoImage(file="C:\\images\\01.gif")
imgB = PhotoImage(file="C:\\images\\02.gif")

# Put the image on the canvas and tell it which image to use
canvas.create_image(10, 10, anchor=NW, image=imgA, activeimage=imgB)
