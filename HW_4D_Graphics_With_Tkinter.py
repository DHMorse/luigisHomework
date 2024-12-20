# HW_4D_Graphics_With_Tkinter
# Luke Norvell

from tkinter import *
import random
root = Tk()
c = Canvas(root, width=800, height=600, bg="#AED6F1")
c.pack()


# Ground
c.create_rectangle(0,600,800,300,fill="#239B56")
# Grass
def create_line(x, y):
    c.create_line(x, y, x, y-10, width=2, fill="#2ecc71")
    c.create_line(x , y, x-5, y-10, width=2, fill="#2ecc71")
    c.create_line(x , y, x+5, y-10, width=2, fill="#2ecc71")

for i in range(50):
    x = random.randint(0, 800)
    y = random.randint(300, 600)
    create_line(x, y)

# Tree
c.create_rectangle(750, 500, 700, 400, fill="#a04000")
c.create_polygon(675, 425, 725, 185, 775, 425, fill="#0b5345")

########################################HOUSE########################################
# Base                                                                              #
c.create_rectangle(50, 300, 350, 100, fill="#f9e79f")                               #
# Roof                                                                              #
c.create_polygon(35, 100, 200, 50, 365, 100, fill="#17202a",width=2)                #
# Window                                                                            #
c.create_rectangle(75, 250, 125, 175,fill="#d4e6f1")                                #
c.create_line(100, 250, 100, 175, fill="#2e4053")                                   #
c.create_line(75, 215, 125, 215, fill="#2e4053")                                    #
# Door                                                                              #
c.create_rectangle(300, 300, 245, 200, fill="#6e2c00")                              #
# Doorknob                                                                          #
c.create_arc(290, 245, 295, 250,width=2,outline="#000000")                          #
# Steps to the door                                                                 #
c.create_rectangle(300, 300, 245, 325, fill="#5d6d7e")                              #
c.create_rectangle(300, 325, 245, 350, fill="#5d6d7e")                              #
c.create_rectangle(300, 350, 245, 375, fill="#5d6d7e")                              #
# Garage                                                                            #
c.create_rectangle(350, 300, 360, 100, fill="#616a6b")                              #
c.create_rectangle(350, 300, 650, 290, fill="#616a6b")                              #
#####################################################################################

# Sun
c.create_arc(775, 25, 700, 100, outline="#f1c40f",style=CHORD, extent=359.9, fill="#f1c40f")

# Car (taken from one of the lessons)
c.create_polygon(400, 280, 412, 280, 420, 267, 440, 267, 448, 280, 512, 280, 520, 267, 540, 267, 548, 280, 557, 280, 548, 260, 500, 255, 480, 240, 440, 240, 415, 255, outline="#145a32", width=2,fill="#145a32")
c.create_arc(420, 270, 440, 290, extent=359.9, width=6, outline="Gray", style=ARC)
c.create_arc(520, 270, 540, 290, extent=359.9, width=6, outline="Gray", style=ARC)
c.create_polygon(418, 256, 497, 256, 477, 242, 442, 242, outline="Gray", width=1)

mainloop()