# Encrypt1.py

def encrypt123(s):
    s = s.upper()
    output = ""
    for ch in s:
        num = ord(ch) - 64
        output += str(num) + " "
    return output

def decrypt123(s):
    output = ""
    nums = s.split()
    nums = s.split()
    for n in nums:
        x = int(n) + 64
        output += chr(x)
    return output


# plain_text = input("Type something: ")
# encrypted_text = encrypt123(plain_text)
# print(encrypted_text)

encrypted_text = input("Type something: ")
plain_text = decrypt123(encrypted_text)
print(plain_text)

