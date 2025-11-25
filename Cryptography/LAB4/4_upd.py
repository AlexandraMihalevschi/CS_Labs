#!/usr/bin/env python3

# Initial Permutation table (DES IP)
INITIAL_PERMUTATION_TABLE = [
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6
]

def ascii_to_bin(text):
    """Convert 8 ASCII chars to 64-bit binary string"""
    return ''.join(f'{ord(c):08b}' for c in text)

def permute(block, table):
    return ''.join(block[i] for i in table)

def get_L1(msg_text):
    # 1. Convert message to 64-bit binary
    msg_bin = ascii_to_bin(msg_text)

    # 2. Initial Permutation
    after_ip = permute(msg_bin, INITIAL_PERMUTATION_TABLE)

    # 3. Split into L0 and R0
    L0 = after_ip[:32]
    R0 = after_ip[32:]

    print("Message:", msg_bin)
    print("Message after ip:", after_ip)
    print("L0:", L0)
    print("R0:", R0)

    # 4. DES rule: L1 = Rn-1
    L1 = R0

    return L1


# Run script
if __name__ == "__main__":
    print("Compute L1 for DES (first round)\n")
    message = input("Enter 8-character message: ").strip()

    if len(message) != 8:
        print("Error: Message must be exactly 8 characters!")
    else:
        L1 = get_L1(message)
        print("\nL1 =", L1)
