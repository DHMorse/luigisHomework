# Feed_the_Sprats.py

from tkinter import *
from Person import *

root = Tk()
s1 = StringVar()
s2 = StringVar()

jack = Person("Jack", 70, 150, 1)
joan = Person("Joan", 63, 240, 3)

def button1_click():
    jack.eat()
    s1.set(jack.name + ": " + str(jack.weight))

def button2_click():
    joan.eat()
    s2.set(joan.name + ": " + str(joan.weight))

label1 = Label(root, textvariable=s1,width=10,height=3)
label2 = Label(root, textvariable=s2,width=10,height=3)
button1 = Button(root, text="Feed Jack", command=button1_click)
button2 = Button(root, text="Feed Joan", command=button2_click)

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)

root.mainloop()