# Create_Raw.py

f = open("image1.raw", "wb")
b = bytes([0, 0, 200])
for i in range(0, 120000):
    f.write(b)
f.close()
