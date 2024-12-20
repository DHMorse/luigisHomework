# CS_HW_2G_Twenty_Letters
# Luke Norvell

# Open the file
f = open("C:\\Users\\Luke\\Documents\\CS\\Chapter02\\work\\words.txt")

# Make a list
words = []

# Loop through the file and find all words with 20 or more letters
for twenty in f:
    twenty = twenty.strip()
    if len(twenty) >= 20:
        words.append(twenty) # Store the word in the list "words"

# Sort the list
words.sort()

# Make a variable to find the total
count = 0

# Display all the words
for display in words:
    print(display)
    count += 1 # Every time a word is found, add one to the total amount of words

# Print the number of words found
print("Number of words found:", count) 

# Close the file
f.close()