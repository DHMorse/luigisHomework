# Count_Lines.py

# Open the file
f = open("words.txt")

n = 0
# Count the number of lines in the file
for line in f:
    n = n + 1
print(n)

# Close the file
f.close();
