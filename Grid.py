# Grid.py

from tkinter import *
root = Tk()
s1 = StringVar()
s2 = StringVar()
s1.set("1")
s2.set("2")

def button1_click():
    s1.set("A")

def button2_click():
    s2.set("B")
label1 = Label(root, textvariable=s1)
label2 = Label(root, textvariable=s2)
button1 = Button(root, text="Button 1", command=button1_click)
button2 = Button(root, text="Button 2", command=button2_click)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
