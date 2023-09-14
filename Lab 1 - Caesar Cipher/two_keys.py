choice = input("Select e for encryption or d for decryption: ")
key1 = int(input("Input the key1: (1 - 25): "))
key2 = input("Enter key2: at least 7 letters: ")
message = input("Enter the message: ")

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_alphabet(key2):
    key2 = key2.upper()
    letters = []
    for letter in key2:
        if letter not in letters:
            letters.append(letter)
    result = [letter for letter in alphabet if letter not in letters]
    new_alphabet = ''.join(letters + result)
    return new_alphabet

def caesar_cipher_2key(message, key1, key2, choice):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper().replace(' ', '')

    if not (1 <= key1 <= 25) or not (7 <= len(key2) <= 26) or not key2.isalpha():
        print("Key 2: has to have no less than 7 letters")
        return

    if choice == 'e':
        new_alphabet = create_alphabet(key2)
        print("New alphabet:", new_alphabet)
        encrypted_string = ""
        for char in message:
            if char != " ":
                e = (new_alphabet.index(char) + key1) % 26
                encrypted_string = encrypted_string + new_alphabet[e]
        return encrypted_string

    elif choice == 'd':
        new_alphabet = create_alphabet(key2)
        decrypted_string = ""
        for char in message:
            if char != " ":
                d = (new_alphabet.index(char) - key1) % 26
                decrypted_string = decrypted_string + new_alphabet[d]
        return decrypted_string

    else:
        print("Error, choose encrypt or decrypt")

if choice in ['e', 'd']:
    result = caesar_cipher_2key(message, key1, key2, choice)
    if result:
        print("Result: " + result)
else:
    print("Error, choose encrypt or decrypt")

