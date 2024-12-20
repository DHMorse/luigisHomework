#Read_File.py

#Open the file
f = open("usaconst.txt")

#Read a line and display it
line = f.readline()
line = line.strip()
print(line)

line = f.readline()
line = line.strip()
print(line)

#Close the file
f.close()



