# Vowel.py

def is_vowel(ch):
    ch = ch.lower()
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return True
    else:
        return False
def num_vowels(s):
    count = 0
    for letter in s:
        if is_vowel(letter):
            count = count + 1
    return count


print(num_vowels("This is another test"))
