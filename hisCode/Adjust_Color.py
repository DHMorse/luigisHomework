# Adjust_Color.py

f = open("Sailbot.raw", "rb")

# Create a bytearray to store the output data
output = bytearray()

# Loop through the file
# Set the variable b to a non-zero value so the while loop will start
b = 1
while b:
    # read two bytes
    b = f.read(2)
    output.extend(b)
    # read the third byte, which will be the blue component
    b = f.read(1)
    if b:
        # increase the value by 10%
        num = int(b[0] * 1.1)
        if num > 255:
            num = 255
        output.append(num)

f.close()

f = open("Sailboat2.raw", "wb")
f.write(output)
f.close()
