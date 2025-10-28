ALPHABET = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"

def check_input(text):
    allowed = set(ALPHABET.lower() + ALPHABET)
    text_chars = set(text)
    
    if not text_chars.issubset(allowed):
        bad_chars = text_chars - allowed
        print(f"Error: Invalid characters found: {bad_chars}")
        print(f"Allowed characters are: A-Z, a-z, Ă, Â, Î, Ș, Ț")
        return False
    return True

def check_key_length(key):
    if len(key) < 7:
        print(f"Error: Key must have at least 7 characters. Current length: {len(key)}")
        return False
    return True

def clean_key(key):
    result = ""
    seen = set()
    
    for char in key.upper():
        if char in ALPHABET and char not in seen:
            result += char
            seen.add(char)
    
    return result

def make_matrix(key):
    clean = clean_key(key)
    
    rest = ""
    for letter in ALPHABET:
        if letter not in clean:
            rest += letter
    
    full = clean + rest
    
    matrix = []
    for i in range(5):
        row = []
        for j in range(6):
            if i * 6 + j < len(full):
                row.append(full[i * 6 + j])
            else:
                row.append('')
        matrix.append(row)
    
    positions = {}
    for i in range(5):
        for j in range(6):
            if matrix[i][j]:
                positions[matrix[i][j]] = (i, j)
    
    return matrix, positions

def clean_text(text):
    result = ""
    for char in text.upper():
        if char in ALPHABET:
            result += char

    fixed = ""
    i = 0
    while i < len(result):
        c1 = result[i]
        if i + 1 < len(result):
            c2 = result[i + 1]
            if c1 == c2:
                sep = 'X' if c1 != 'X' else 'Z'
                fixed += c1 + sep
                i += 1
            else:
                fixed += c1 + c2
                i += 2
        else:
            fixed += c1 + ('X' if c1 != 'X' else 'Z')
            i += 1

    return fixed

def encrypt_pair(c1, c2, matrix, positions):
    r1, col1 = positions[c1]
    r2, col2 = positions[c2]
    
    if r1 == r2:
        new_c1 = (col1 + 1) % 6
        new_c2 = (col2 + 1) % 6
        return matrix[r1][new_c1] + matrix[r2][new_c2]
    
    elif col1 == col2:
        new_r1 = (r1 + 1) % 5
        new_r2 = (r2 + 1) % 5
        return matrix[new_r1][col1] + matrix[new_r2][col2]
    
    else:
        return matrix[r1][col2] + matrix[r2][col1]

def decrypt_pair(c1, c2, matrix, positions):
    r1, col1 = positions[c1]
    r2, col2 = positions[c2]
    
    if r1 == r2:
        new_c1 = (col1 - 1) % 6
        new_c2 = (col2 - 1) % 6
        return matrix[r1][new_c1] + matrix[r2][new_c2]
    
    elif col1 == col2:
        new_r1 = (r1 - 1) % 5
        new_r2 = (r2 - 1) % 5
        return matrix[new_r1][col1] + matrix[new_r2][col2]
    
    else:
        return matrix[r1][col2] + matrix[r2][col1]

def encrypt(message, key):
    if not check_key_length(key):
        return ""
    
    if not check_input(message):
        return ""
    
    matrix, positions = make_matrix(key)
    text = clean_text(message)
    
    result = ""
    for i in range(0, len(text), 2):
        c1 = text[i]
        c2 = text[i + 1]
        result += encrypt_pair(c1, c2, matrix, positions)
    
    return result

def decrypt(message, key):
    if not check_key_length(key):
        return ""
    
    if not check_input(message):
        return ""
    
    matrix, positions = make_matrix(key)
    
    result = ""
    for i in range(0, len(message), 2):
        c1 = message[i]
        c2 = message[i + 1]
        result += decrypt_pair(c1, c2, matrix, positions)
    
    return result

def main():
    print("=== Playfair Cipher for Romanian Language ===")
    print("Romanian alphabet: A-Z, Ă, Â, Î, Ș, Ț (31 letters)")
    print()
    
    while True:
        print("\nOptions:")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("\nChoose option (1-3): ").strip()
        
        if choice == "1":
            key = input("Enter key (minimum 7 characters): ").strip()
            plaintext = input("Enter message to encrypt: ").strip()
            
            result = encrypt(plaintext, key)
            if result:
                print(f"\nEncrypted message: {result}")
                print("Note: Spaces and punctuation must be added manually.")
        
        elif choice == "2":
            key = input("Enter key (minimum 7 characters): ").strip()
            ciphertext = input("Enter ciphertext to decrypt: ").strip()
            
            result = decrypt(ciphertext, key)
            if result:
                print(f"\nDecrypted message: {result}")
                print("Note: Spaces and punctuation must be added manually.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()