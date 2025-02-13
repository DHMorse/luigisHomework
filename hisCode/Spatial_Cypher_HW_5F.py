# Spatial_Cypher_HW_5F.py
# Luke Norvell
f = open("encrypted.txt", "r")
encrypted_text = f.read()
decrypted_text = encrypted_text[::2]
print(decrypted_text)
f.close()