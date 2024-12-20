# Hellow_Goodbye.py

from tkinter import *

def say_hello():
    print("Hello")

def say_goodbye():
    print("goodbye")
    quit()

root = Tk()
btn1 = Button(root, text="Hello", command=say_hello)
btn1.pack()
btn2 = Button(root, text="Goodbye", command=say_goodbye)
btn2.pack()
root.mainloop()
