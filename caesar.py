import string
from time import sleep

alphabet = string.ascii_letters
i=1
def decrypt(key):
    encrypted_message = input("text eingeben")
    key=i
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c
            
    print(decrypted_message)
for j in range(1):
    decrypt(i)
    i+=1
