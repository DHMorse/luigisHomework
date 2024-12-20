# HW_4A_Rectangle_Loop
# Luke Norvell

from tkinter import *

c = Canvas(width=800, height=600, bg="White")

# Caculate space and stuff
total_rect_width = 20 * 12
remaining_space = 800 - total_rect_width
gap = remaining_space / (12 + 1)

for i in range(12):
    x_pos = (i + 1) * gap + i * 20
    c.create_rectangle(x_pos, 150, x_pos + 20, 250, outline="Blue", width=2,fill="Grey",activefill="Red")

c.pack()
mainloop()
