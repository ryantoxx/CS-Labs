choice = input("Select e for encryption or d for decryption: ")
key = int(input("Input the key (1 - 25): "))
message = input("Enter the message: ")

def caesar_cipher(message, key, choice):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    message = message.upper().replace(' ', '')
    
    if not (1 <= key <= 25):
        print("Input a key bewtween 1 and 25")
        return

    if choice == 'e':
        result = ''
        for i in message:
            if i in alphabet:
                index = (alphabet.index(i) + key) % 26
                result += alphabet[index]
            else:
                print("The symbol " + i +  " is not in the English alphabet")

                continue
        return result
    elif choice == 'd':
        result = ''
        for i in message:
            if i in alphabet:
                index = (alphabet.index(i) - key) % 26
                result += alphabet[index]
            else:
                print("The symbol " + i + " is not in the English alphabet")
                continue
        return result
    else:
        print("Error, choose encrypt or decrypt")

if choice in ['e', 'd']:
    result = caesar_cipher(message, key, choice)
    if result:
        print("Result:" + result)
else:
    print("Error, choose encrypt or decrypt")
