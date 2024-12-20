# Word_Endings.py

# Open the file
f = open("words.txt")

# Count the words in "ing" and "ion"
ing = 0
ion = 0

for line in f:
    word = line.strip()
    if word.endswith("ion"):
        ion = ion + 1
    elif word.endswith("ing"):
        ing = ing + 1

print("ion", ion)
print("ing", ing)

# Close the file
f.close()
