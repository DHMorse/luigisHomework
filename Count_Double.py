# Count_Double.py

# Open the file
f = open("words.txt")

# Find all the words with a double o
# display each word and keep a running total
n = 0
for line in f:
    word = line.strip()
    if word.find("oo") >=0:
        print(word)
        n = n + 1
print("Total:", n)

#Close the file
f.close();
