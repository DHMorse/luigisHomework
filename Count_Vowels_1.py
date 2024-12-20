# Count_Vowels.py

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
        if word[i] == "a":
            vowels["a"] = vowels["a"] + 1
        elif word[i] == "e":
            vowels["e"] = vowels["e"] + 1
        elif word[i] == "o":
            vowels["o"] = vowels["o"] + 1
        elif word[i] == "i":
            vowels["i"] = vowels["i"] + 1
        elif word[i] == "u":
            vowels["u"] = vowels["u"] + 1

print("a:", vowels["a"])
print("e:", vowels["e"])
print("i:", vowels["i"])
print("o:", vowels["o"])
print("u:", vowels["u"])

# Close the file
f.close();
