# CS_HW_3C_String_Info
# Luke Norvell

def string_info(string):
    # Make the variables that will be assigned to the different characteristics of the string
    total_chars = len(string)
    total_words = 1
    total_digits = 0
    total_letters = 0
    for i in string:
        if i == ' ':
            total_words += 1

        elif i in '0123456789':
            total_digits += 1

        elif i.lower() in 'abcdefghijklmnopqrstuvwxyz':
            total_letters += 1

    print("String Info:")
    print("characters:",(total_chars))
    print("words:",(total_words))
    print("digits:",(total_digits))
    print("letters:",(total_letters))

string = input("Type a word or phrase: ")
string_info(string)