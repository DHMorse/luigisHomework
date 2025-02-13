# Color_Schemes.py
import json
f = open("color_schemes.json", "r")
data = json.load(f)
f.close()

# The JSON data is a dictionary with one entry, schemes.
# Get this entry, which is a list
schemes = data["schemes"]

# Loop through each item in the list
for scheme in schemes:
    name = scheme["name"]      # ths will be a string
    colors = scheme["colors"]  # this will be a dictionary

    # Get the three colors
    light = colors["light"]
    medium = colors["medium"]
    dark = colors["dark"]

    # Display the data
    print(name)
    print(light)
    print(medium)
    print(dark)
