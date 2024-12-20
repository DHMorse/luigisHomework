# CS_HW_2J_Palindrome
# Luke Norvell

print("Palindrome Tester")
raw_input = input("Type a word: ")
word = raw_input.lower()
length = len(word)
half_length = length // 2
is_palindrome = True

for i in range(half_length):
    if word[i] != word[length - 1 - i]:
        is_palindrome = False

if is_palindrome == True:
    print("The word provided is a palindrome.")

else:
    print("The word provided is not a palindrome.")