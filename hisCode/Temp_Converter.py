# Temp_Converter.py

# Convert Fahrenheit temperature to Celsius
def FtoC(tempF):
    tempC = (5/9)*(tempF - 32)
    return tempC

s = input("Temp in degrees Fahrenheit? ")
# convert the string to a float
fahrenheit = float(s)

# call the function to convert to Celsius
celsius = FtoC(fahrenheit)
print("Temp in degress Celsius:", celsius)
