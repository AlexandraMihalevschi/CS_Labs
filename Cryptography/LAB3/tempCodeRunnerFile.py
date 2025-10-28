class PlayfairCipher:
    ROMANIAN_ALPHABET = "AĂÂBDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
    
    def __init__(self):
        self.key_matrix = []
        self.alphabet_positions = {}
    
    def validate_input(self, text):
        allowed_chars = set(self.ROMANIAN_ALPHABET.lower() + self.ROMANIAN_ALPHABET)
        text_chars = set(text)
        
        if not text_chars.issubset(allowed_chars):
            invalid_chars = text_chars - allowed_chars
            print(f"Error: Invalid characters found: {invalid_chars}")
            print(f"Allowed characters are: A-Z, a-z, Ă, Â, Î, Ș, Ț")
            return False
        return True
    
    def validate_key_length(self, key):
        if len(key) < 7:
            print(f"Error: Key must have at least 7 characters. Current length: {len(key)}")
            return False
        return True
    
    def prepare_key(self, key):
        prepared_key = ""
        seen = set()
        
        for char in key.upper():
            if char in self.ROMANIAN_ALPHABET and char not in seen:
                prepared_key += char
                seen.add(char)
        
        return prepared_key
    
    def build_key_matrix(self, key):
        prepared_key = self.prepare_key(key)
        
        remaining_letters = ""
        for letter in self.ROMANIAN_ALPHABET:
            if letter not in prepared_key:
                remaining_letters += letter
        
        full_alphabet = prepared_key + remaining_letters
        
        self.key_matrix = []
        for i in range(5):
            row = []
            for j in range(6):
                if i * 6 + j < len(full_alphabet):
                    row.append(full_alphabet[i * 6 + j])
                else:
                    row.append('')
            self.key_matrix.append(row)
        
        self.alphabet_positions = {}
        for i in range(5):
            for j in range(6):
                if self.key_matrix[i][j]:
                    self.alphabet_positions[self.key_matrix[i][j]] = (i, j)
    
    def prepare_text(self, text):
        cleaned_text = ""
        for char in text.upper():
            if char in self.ROMANIAN_ALPHABET:
                cleaned_text += char
        
        processed_text = ""
        i = 0
        while i < len(cleaned_text):
            if i + 1 < len(cleaned_text):
                char1 = cleaned_text[i]
                char2 = cleaned_text[i + 1]
                
                processed_text += char1
                
                if char1 == char2:
                    separator = 'Z' if char1 == 'X' else 'X'
                    processed_text += separator
                    processed_text += char2
                    i += 2
                else:
                    processed_text += char2
                    i += 2
            else:
                processed_text += cleaned_text[i]
                processed_text += 'X' if cleaned_text[i] != 'X' else 'Z'
                i += 1
        
        return processed_text
    
    def get_position(self, char):
        """Get position of character in key matrix"""
        return self.alphabet_positions[char]
    
    def encrypt_pair(self, char1, char2):
        """Encrypt a pair of characters"""
        row1, col1 = self.get_position(char1)
        row2, col2 = self.get_position(char2)
        
        if row1 == row2:
            # Same row - shift right
            new_col1 = (col1 + 1) % 6
            new_col2 = (col2 + 1) % 6
            return self.key_matrix[row1][new_col1] + self.key_matrix[row2][new_col2]
        
        elif col1 == col2:
            # Same column - shift down
            new_row1 = (row1 + 1) % 5
            new_row2 = (row2 + 1) % 5
            return self.key_matrix[new_row1][col1] + self.key_matrix[new_row2][col2]
        
        else:
            # Rectangle - swap columns
            return self.key_matrix[row1][col2] + self.key_matrix[row2][col1]
    
    def decrypt_pair(self, char1, char2):
        """Decrypt a pair of characters"""
        row1, col1 = self.get_position(char1)
        row2, col2 = self.get_position(char2)
        
        if row1 == row2:
            # Same row - shift left
            new_col1 = (col1 - 1) % 6
            new_col2 = (col2 - 1) % 6
            return self.key_matrix[row1][new_col1] + self.key_matrix[row2][new_col2]
        
        elif col1 == col2:
            # Same column - shift up
            new_row1 = (row1 - 1) % 5
            new_row2 = (row2 - 1) % 5
            return self.key_matrix[new_row1][col1] + self.key_matrix[new_row2][col2]
        
        else:
            # Rectangle - swap columns
            return self.key_matrix[row1][col2] + self.key_matrix[row2][col1]
    
    def print_key_matrix(self):
        """Print the key matrix for debugging"""
        print("\nKey Matrix (5x6):")
        for row in self.key_matrix:
            print(" ".join(row))
        print()


def playfair_encrypt(message, key):
    cipher = PlayfairCipher()
    
    if not cipher.validate_key_length(key):
        return ""
    
    if not cipher.validate_input(message):
        return ""
    
    cipher.build_key_matrix(key)
    prepared_text = cipher.prepare_text(message)
    
    ciphertext = ""
    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]
        ciphertext += cipher.encrypt_pair(char1, char2)
    
    return ciphertext


def playfair_decrypt(message, key):
    cipher = PlayfairCipher()
    
    if not cipher.validate_key_length(key):
        return ""
    
    if not cipher.validate_input(message):
        return ""
    
    cipher.build_key_matrix(key)
    
    plaintext = ""
    for i in range(0, len(message), 2):
        char1 = message[i]
        char2 = message[i + 1]
        plaintext += cipher.decrypt_pair(char1, char2)
    
    return plaintext


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
            
            result = playfair_encrypt(plaintext, key)
            if result:
                print(f"\nEncrypted message: {result}")
                print("Note: Spaces and punctuation must be added manually.")
        
        elif choice == "2":
            key = input("Enter key (minimum 7 characters): ").strip()
            ciphertext = input("Enter ciphertext to decrypt: ").strip()
            
            result = playfair_decrypt(ciphertext, key)
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

