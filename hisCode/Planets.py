# Planets.py

import requests
import json

number = input("Enter a planet numner (1 to 9): ")

# request the data from the web app
data = requests.get(f"https://derekowens.com/cs/planets.aspx?num={number}")

planet = json.loads(data.text)

for key in planet:
    output = key + f": {planet[key]}"

for key in planet:
    if key=="radius":
        output = output + " km"
    if key=="mass":
        output += " Earth masses"
        mass = planet[key] * 5.98 * 10**24
        output += f", {mass} kg"
    if key=="orbit_radius":
        output += " AU"
        radius = planet[key] * 1.5 * 10**8
        output += f", {radius} km"
    if key=="period":
        output += " Earth years"
        period = planet[key] * 365.2425
        output += f", {period} days"
    if key=="gravity":
        output += " times Earth's"
        gravity = planet[key] * 9.8
        output += f", {gravity} m/s^2"

print(output)
        
