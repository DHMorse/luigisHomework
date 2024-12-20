# Count_Vowels_alternate.py

# Open the file
f = open("words.txt")

# create a map
vowels = { "a" : 0,
           "e" : 0,
           "i" : 0,
           "o" : 0,
           "u" : 0 }

# Examine each word and find the vowels
for line in f:
    word = line.strip()
    for i in range(0 , len(word)):
        if word[i] == "a" or word[i] == "e" or word[i] == "i" or word[i] == "o" or word[i] == "u":
            vowels[word[i]] = vowels[word[i]] + 1

for k in vowels:
    print(k, ":", vowels[k])

# Close the file
f.close();
