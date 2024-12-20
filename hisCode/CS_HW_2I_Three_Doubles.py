# CS_HW_2I_Three_Doubles.py
# Luke Norvell

# Open the file
f = open("C:\\Users\\Luke\\Documents\\CS\\Chapter02\\work\\words.txt")

total = 0
for line in f:
    word = line.strip()
    double_tracker = 0
    i = 0  # Variable for looking at the word
    while i < len(word) - 1:
        if word[i] == word[i + 1]:  # Check for consecutive letters
            double_tracker += 1
            i += 2  # Skip the next letter (to avoid overlapping doubles)
        else:
                i += 1  # Move to the next letter
    if double_tracker >= 3:
        print(word)
        total += 1

print("Number of words found with three or more sets of double letters:", total)


# Close the file
f.close()