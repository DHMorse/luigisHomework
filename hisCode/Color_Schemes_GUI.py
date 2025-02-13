# Color_Schemes_GUI.py

import tkinter
import json

root = tkinter.Tk()

# Get info from the file
f = open("color_schemes.json", "r")
data = json.load(f)
f.close()

# Create an empty list to hold the tkinter frame objects
frames = []

# The JSON data is a dictionary with one entry, schemes.
schemes = data["schemes"]

# Loop through each item in the list
i = 0
for scheme in schemes:
    name = scheme["name"]      # ths will be a string
    colors = scheme["colors"]  # this will be a dictionary
    
    # Get the three colors. Each of these will be a hex color string
    light = colors["light"]
    medium = colors["medium"]
    dark = colors["dark"]

    # Put all the info in a Tkinter frame
    frames.append(tkinter.Frame(root, width=300, height=200,bg="#F0F0F0"))
    label = tkinter.Label(frames[i], text = name)
    label.grid(row=0, column=0)

    color1 = tkinter.Label(frames[i], text=light, bg=light,
                           fg=dark,padx=10, pady=10)
    color1.grid(row=1, column=0, padx=10, pady=10)
    
    color2 = tkinter.Label(frames[i], text=medium, bg=medium,
                           fg=light,padx=10, pady=10)
    color2.grid(row=1, column=1, padx=10, pady=10)
    
    color3 = tkinter.Label(frames[i], text=dark, bg=dark,
                           fg=light,padx=10, pady=10)
    color3.grid(row=1, column=2, padx=10, pady=10)
    
    # Display the data
    print(name)
    print(light)
    print(medium)
    print(dark)
    i += 1

# Put the frames in a grid layout
frames[0].grid(row=0, column=0, padx=10, pady=10)
frames[1].grid(row=1, column=0, padx=10, pady=10)
frames[2].grid(row=2, column=0, padx=10, pady=10)
frames[3].grid(row=3, column=0, padx=10, pady=10)
mainloop()
