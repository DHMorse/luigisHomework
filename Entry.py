# Entry.py

from tkinter import *
root = Tk()
canvas = Canvas(root, width=640, height=480, bg="#808080")
canvas.pack()


e = Entry(root)
e.pack()

def display_image():
    f = e.get()
    print(f)
    global img
    img = PhotoImage(file=f)
    canvas.create_image(0, 0, anchor=NW, image=img)
    

b = Button(root, text="Show", command=display_image)
b.pack()

mainloop()
