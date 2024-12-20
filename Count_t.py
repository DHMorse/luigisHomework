# Count_t.py

# Open file
f = open("words.txt")

# Count the total number of t's in each word
n = 0
for line in f:
    # look at each word, strip of the EOL character
    # and convert to lower case
    word = line.strip()
    word = word.lower()
    # look at each letter
    for i in range(0, len(word)):
        if word[i] == "t":
            n = n + 1
print("The letter t occurs", n, "times.")

# Close the file
f.close();
