# Label.py
from tkinter import *

root = Tk()
sv = StringVar()

def button1_click():
    sv.set("Hi")

def button2_click():
    sv.set("There")

label1 = Label(root, bg="Green", fg="White",
               width=6, height=6, bd=8,font="Arial 16",
               anchor=CENTER, textvariable=sv)

sv.set("Label")


button1 = Button(root, text="Hi", command=button1_click)
button2 = Button(root, text="There", command=button2_click)

button1.pack()
button2.pack()
label1.pack()
mainloop()
