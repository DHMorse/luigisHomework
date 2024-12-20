# Boing.py

from tkinter import *
from random import *
root = Tk()
canvas_width = 600
canvas_height = 400
canvas = Canvas(root, width=canvas_width, height=canvas_height,
                bg="black")
canvas.pack()

class Ball:
    # A Ball Object will have an x position, a y position,
    # a radius, and a color
    def __init__(self, x, y, r, c, xvel, yvel):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.xvel = xvel
        self.yvel = yvel
        self.circle = canvas.create_arc(x-r, y-r, x+r, y+r,
                                        extent=359, width=1,
                                        style=PIESLICE, outline = c, fill = c)
    def move(self):
        self.yvel = self.yvel + 0.2
        self.x = self.x + self.xvel
        self.y = self.y + self.yvel
        self.xvel = self.xvel * 0.998
        self.yvel = self.yvel * 0.998
        self.check_for_wall_hit()
        canvas.coords(self.circle, self.x - self.r, self.y - self.r,
                      self.x + self.r, self.y + self.r)
        canvas.after(10, self.move)

    def check_for_wall_hit(self):
        if self.x < self.r:
            self.xvel = -self.xvel
            self.x = self.x + 2*(self.r - self.x)
        if self.x > canvas_width - self.r:
            self.xvel = -self.xvel
            self.x = self.x - 2*(self.x + self.r - canvas_width)
        if self.y < self.r:
            self.yvel = -self.yvel
            self.y = self.y + 2*(self.r - self.y)
        if self.y > canvas_height - self.r:
            self.yvel = -self.yvel
            self.y = self.y - 2*(self.y + self.r - canvas_height)


# Make an empty list to hold the Ball objects
ball = []
n = 10
for i in range(0, n):
    # create a random color by making a random Hex string
    color = "#"
    hexdigits = "ABCDEF0123456789"
    for j in range(0, 6):
        color = color + choice(hexdigits)
    # get some random vlaues for position, velocity, and radius
    radius = randrange(3, 24)
    x = randrange(100, 500)
    y = randrange(50, 350)
    xvel = randrange(-8, 8)
    yvel = randrange(-8, 8)
    b = Ball(x, y, radius, color, xvel, yvel)
    ball.append(b)

for i in range (0,n):
    ball[i].move()

mainloop()
