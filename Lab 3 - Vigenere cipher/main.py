choice = input("Select e for encryption or d for decryption: ")
key = input("Input the key: ")
message = input("Enter the message: ")

def is_valid_key(key):
    return key.isalpha()

def is_valid_message(message, alphabet):
    return all(char in alphabet for char in message)

def vigenere_cipher(message, key, choice):
    alphabet = 'AĂÂBCDEFGHIÎJKLMNOPQRSŞTȚUVWXYZ'
    message = message.upper().replace(' ', '')

    if len(key) < 7:
        print("Key length must be at least 7 letters.")
        return
    
    if not is_valid_key(key):
        print("Key must consist of letters only.")
        return
    
    if not is_valid_message(message, alphabet):
        print("Message must consist of letters from the Romanian alphabet: " + alphabet)
        return
    
    if choice == 'e':
        result = ''
        key_index = 0
        for i in message:
            if i in alphabet:
                key_letter = key[key_index % len(key)].upper()
                key_num = alphabet.index(key_letter)
                message_num = alphabet.index(i)
                encrypted_num = (message_num + key_num) % 31
                result += alphabet[encrypted_num]
                key_index += 1
            else:
                print("The symbol " + i + " is not in the Romanian alphabet")
                continue
        return result
    elif choice == 'd':
        result = ''
        key_index = 0
        for i in message:
            if i in alphabet:
                key_letter = key[key_index % len(key)].upper()
                key_num = alphabet.index(key_letter)
                message_num = alphabet.index(i)
                decrypted_num = (message_num - key_num) % 31
                result += alphabet[decrypted_num]
                key_index += 1
            else:
                print("The symbol " + i + " is not in the Romanian alphabet")
                continue
        return result
    else:
        print("Error, choose encrypt or decrypt")


if choice in ['e', 'd']:
    result = vigenere_cipher(message, key, choice)
    if result:
        print("Result: " + result)
else:
    print("Error, choose encrypt or decrypt")
