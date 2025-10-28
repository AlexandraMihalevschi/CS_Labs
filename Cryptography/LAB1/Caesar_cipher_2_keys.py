from collections import OrderedDict

def get_message_for_encryption(message:str):
    message = message.upper()

    clean_message = ""
    for char in message:
        if char.isalpha() or char == ' ':
            clean_message += char

    if len(clean_message) != len(message):
        return "Use characters A-Z or a-z!"

    return clean_message

def update_alphabet(key):
    alphabet = "".join(OrderedDict.fromkeys(get_message_for_encryption(key) + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print(alphabet)
    return alphabet

def encrypt_message(message, key, alphabet):
    encrypted_message = ""
    for char in message:
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                new_position = (i + key) % 26
                encrypted_char = alphabet[new_position]
                encrypted_message += encrypted_char
    return print(encrypted_message)

def decrypt_message(message, key, alphabet):
    decrypted_message = ""
    for char in message:
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                new_position = (i - key) % 26
                encrypted_char = alphabet[new_position]
                decrypted_message += encrypted_char
    return print(decrypted_message)


secret = get_message_for_encryption(str(input("Enter the secret message: ")))

shift = int(input("Enter the shift value: "))
word_key = str(input("Enter the 2nd key value: "))
if len(word_key) < 7 or (shift < 1) or (shift > 25) or (secret == 'Use characters A-Z or a-z!'):
    exit('Invalid input')

new_alphabet =  update_alphabet(word_key)
operation_choice = int(input("Enter the operation choice: \n[1] encryption \n[2] decryption \n[3] both\n-->"))
if operation_choice == 1:
    print(f"Encrypted message:")
    encrypt_message(secret, shift, new_alphabet)
elif operation_choice == 2:
    print(f"Decrypted message:")
    decrypt_message(secret, shift, new_alphabet)
elif operation_choice == 3:
    print(f"Encrypted message:")
    encrypt_message(secret, shift, new_alphabet)
    print(f"Decrypted message:")
    decrypt_message(secret, shift, new_alphabet)
else:
    print("Invalid choice!")
