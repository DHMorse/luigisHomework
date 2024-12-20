from tkinter import *
root = Tk()

canvas = Canvas(root, width=400, height=300, bg="#000000")
canvas.pack()
x1 = 150
y1 = 100
x2 = 250
y2 = 200

class ResizeRect:
    def __init__(self, x1, y1, x2 ,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.rect = canvas.create_rectangle(0,0,1,1)

    def draw(self):
        canvas.delete(self.rect)
        self.rect = canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                            outline="#00B000", width=2)
        root.update()
        
    def narrower(self):
        self.x1 = self.x1 + 5
        self.x2 = self.x2 - 5
        print(self.x1, self.x2)
        self.draw()
    
    def wider(self):
        self.x1 = self.x1 - 5
        self.x2 = self.x2 + 5
        print(self.x1, self.x2)
        self.draw()

r = ResizeRect(150, 100, 250, 200)
r.draw()

def left(event):
    r.narrower()
    print("Narrow")

def right(event):
    r.wider()
    print("Wider")

canvas.bind_all('<KeyPress-Left>', left)
canvas.bind_all('<KeyPress-Right>', right)

mainloop()