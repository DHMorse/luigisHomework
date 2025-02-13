# Encrypt4.py

from tkinter import *
from tkinter.scrolledtext import *
from crypto import *
root = Tk()
canvas = Canvas(root, width=800, height=600)

# Some basic labels
label_plain = Label(root, text="Plain Text")
label_encrypted = Label(root, text="Encrpyted Text")

label_plain.grid(row=0, column=0, pady=(10,0))
label_encrypted.grid(row=0, column=2, pady=(10,0))

# Create two ScrolledText objects
textbox_plain = ScrolledText(root, width=30, height=10,
                             bg="#DDFFDD")
textbox_encrypted = ScrolledText(root, width=30, height=10,
                             bg="#DDDDFF")

textbox_plain.grid(row=1, column=0, padx=10, pady=10)
textbox_encrypted.grid(row=1, column=2, padx=10, pady=10)

def encrypt():
    plain = textbox_plain.get(1.0, "end-1c")
    encrypted = Crypto.encrypt_xor(plain)
    textbox_encrypted.delete(1.0, "end")
    textbox_encrypted.insert(1.0, encrypted)

def decrypt():
    encrypted = textbox_encrypted.get(1.0, "end-1c")
    decrypted = Crypto.encrypt_xor(encrypted)
    textbox_plain.delete(1.0, "end")
    textbox_plain.insert(1.0, decrypted)


frame1 = Frame(root)
frame1.grid(row=1, column=1)

button_encrypt = Button(frame1, text="Encrypt >>", command=encrypt)
button_decrypt = Button(frame1, text="<< Decrypt", command=decrypt)

button_encrypt.grid(row=0, column=0, padx=10, pady=10)
button_decrypt.grid(row=1, column=0, padx=10, pady=10)

mainloop()
