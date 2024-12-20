from tkinter import *
root = Tk()
canvas = Canvas(root, width=400, height=300, bg="#FFFFFF")
r = canvas.create_rectangle(5, 125, 40, 175, outline="#000000", width=3)
canvas.pack()
for i in range(0, 20):
    canvas.move(r, 18, 2)
mainloop()