# crypto Module for HW_5D.py
# Luke Norvell

class Crypto:
        # Homework 5D function
    def endecrypt_full(s):
        output = ""
        for ch in s:
            if 32 <= ord(ch) <= 126:
                num = ord(ch) + 47
                if num > 126:
                    num -= 94
                output += chr(num)
            else:
                output += ch
        return output
    
    # You can ignore all of this Mr. Owens :)
    cipher = {
            'A':'H',
            'B':'L',
            'C':'B',
            'D':'J',
            'E':'D',
            'F':'Q',
            'G':'S',
            'H':'A',
            'I':'P',
            'J':'Y',
            'K':'G',
            'L':'R',
            'M':'X',
            'N':'K',
            'O':'M',
            'P':'V',
            'Q':'C',
            'R':'I',
            'S':'T',
            'T':'F',
            'U':'N',
            'V':'Z',
            'W':'U',
            'X':'W',
            'Y':'E',
            'Z':'O',
            ' ':' '
        }
    reverse_cipher = {v:k for k,v in cipher.items()}
    
    def encrypt_map(s, direction):
        output = ""
        s = s.upper()
        for ch in s:
            if direction == "encrypt":
                output += Crypto.cipher[ch]
            elif direction == "decrypt":
                output += Crypto.reverse_cipher[ch]
        return output

    
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
        for n in nums:
            x = int(n) + 64
            output += chr(x)
        return output

    def encrypt_rot3(s):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) + 3
                if num > 90:
                    num -= 26
                output += chr(num)
            else:
                output += " "
        return output

    def encrypt_rotn(s, n):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) + n
                if num > 90:
                    num -= 26
                output += chr(num)
            else:
                output += " "
        return output

    def decrypt_rotn(s, n):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) - n
                if num < 65:
                    num += 26
                output += chr(num)
            else:
                output += " "
        return output

    def decrypt_rot3(s):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) - 3
                if num < 65:
                    num += 26
                output += chr(num)
            else:
                output += " "
        return output

    def encrypt_rot13(s):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) + 13
                if num > 90:
                    num -= 26
                output += chr(num)
            else:
                output += " "
        return output

    def decrypt_rot13(s):
        s = s.upper()
        output = ""
        for ch in s:
            if ch != " ":
                num = ord(ch) - 13
                if num < 65:
                    num += 26
                output += chr(num)
            else:
                output += " "
        return output

    def encrypt_xor(s):
        output = ""
        for ch in s:
            num = ord(ch) ^ 5
            output += chr(num)
        return output
