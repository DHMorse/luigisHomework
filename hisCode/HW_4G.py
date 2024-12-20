from tkinter import *
root = Tk()

x = Label(root, text="Arthur", anchor=CENTER, width=10, height=6)
x.grid(row = 0, column = 0)

f1 = Frame(root)
y = Label(f1, text="King", anchor=N, width=20, height=6)
y.grid(row = 0, column = 0)

f2 = Frame(f1)
a = Button(f2, text="of", width=20, height=2)
a.grid(row = 0, column = 1)
b = Button(f2, text="the", width=20, height=2)
b.grid(row = 1, column = 1)
c = Button(f2, text="Britons", width=20, height=2)
c.grid(row = 2, column = 1)

f1.grid(row = 1, column = 0)
f2.grid(row = 0, column = 1)

mainloop()