def get_message_for_encryption(message:str):
    message = message.upper()

    clean_message = ""
    for char in message:
        if char.isalpha():
            clean_message += char

    if len(clean_message) != len(message):
        print("Use characters A-Z or a-z!")

    return clean_message

def encrypt_message(message, shift):
    encrypted_message = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in message:
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                new_position = (i + shift) % 26
                encrypted_char = alphabet[new_position]
                encrypted_message += encrypted_char
    return print(encrypted_message)

def decrypt_message(message:str, shift:int):
    decrypted_message = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in message:
        for i in range(len(alphabet)):
            if char == alphabet[i]:
                new_position = (i - shift) % 26
                encrypted_char = alphabet[new_position]
                decrypted_message += encrypted_char
    return print(decrypted_message)


secret = get_message_for_encryption(str(input("Enter the secret message: ")))

shift = int(input("Enter the shift value: "))
operation_choice = int(input("Enter the operation choice: \n[1] encryption \n[2] decryption \n[3] both\n-->"))
if operation_choice == 1:
    print(f"Encrypted message:")
    encrypt_message(secret, shift)
elif operation_choice == 2:
    print(f"Decrypted message:")
    decrypt_message(secret, shift)
elif operation_choice == 3:
    print(f"Encrypted message:")
    encrypt_message(secret, shift)
    print(f"Decrypted message:")
    decrypt_message(secret, shift)
else:
    print("Invalid choice!")
