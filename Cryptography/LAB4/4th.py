#!/usr/bin/env python3

BLOCK_SIZE = 64

# --- DES Tables (unchanged) ---
KEY_PERMUTATION_TABLE = [
    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3
]

COMPRESSION_PERMUTATION_TABLE = [
    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31
]

S_BOX_TABLE = [
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

EXPANSION_PERMUTATION_TABLE = [
    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0
]

P_BOX_TABLE = [
    15, 6, 19, 20, 28, 11, 27, 16,
    0, 14, 22, 25, 4, 17, 30, 9,
    1, 7, 23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10, 3, 24
]

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


# --- Helper functions ---
def ascii_to_bin(text):
    """Convert 8 ASCII chars to 64-bit binary string"""
    return ''.join(f'{ord(c):08b}' for c in text)


def permute(block, table): return ''.join(block[i] for i in table)
def xor(a, b): return f'{int(a,2)^int(b,2):0{len(a)}b}'
def split_block(block): return block[:len(block)//2], block[len(block)//2:]


def s_box(block):
    output = ''
    for i in range(8):
        sub = block[i*6:(i+1)*6]
        row = int(sub[0]+sub[-1], 2)
        col = int(sub[1:5], 2)
        output += f'{S_BOX_TABLE[i][row][col]:04b}'
    return output


def fprint(name, val): print(f'{name:>25}: {val}')


# --- Compute L1 ---
def get_L1(key_text, msg_text):
    # 1. Convert to binary
    key_bin = ascii_to_bin(key_text)
    msg_bin = ascii_to_bin(msg_text)

    fprint("INPUT MESSAGE", msg_bin)
    fprint("INPUT KEY", key_bin)

    # 2. Initial permutation
    after_ip = permute(msg_bin, INITIAL_PERMUTATION_TABLE)
    L0, R0 = split_block(after_ip)

    print("\n=== INITIAL PERMUTATION ===")
    fprint("After IP", after_ip)
    fprint("L0", L0)
    fprint("R0", R0)

    # 3. Generate first subkey (simplified)
    key_permuted = permute(key_bin, KEY_PERMUTATION_TABLE)
    fprint("\nKEY PERMUTATION", key_permuted)
    lk, rk = split_block(key_permuted)
    lk = lk[1:] + lk[:1]
    rk = rk[1:] + rk[:1]
    subkey1 = permute(lk + rk, COMPRESSION_PERMUTATION_TABLE)
    fprint("ROUND 1 SUBKEY", subkey1)

    # 4. Expansion of R0
    expansion = permute(R0, EXPANSION_PERMUTATION_TABLE)
    fprint("\nExpansion E(R0)", expansion)

    # 5. XOR with subkey
    xor_out = xor(expansion, subkey1)
    fprint("XOR with Subkey", xor_out)

    # 6. S-box substitution
    sbox_out = s_box(xor_out)
    fprint("S-box Output", sbox_out)

    # 7. P-box permutation
    pbox_out = permute(sbox_out, P_BOX_TABLE)
    fprint("P-box Output", pbox_out)

    # 8. Compute L1 and R1
    R1 = xor(L0, pbox_out)
    L1 = R0

    print("\n=== ROUND 1 RESULT ===")
    fprint("L1 = R0", L1)
    fprint("R1 = L0 XOR f(R0,K1)", R1)

    return L1


# --- Run script ---
if __name__ == "__main__":
    print("Compute L1 for DES (first round)\n")
    message = input("Enter 8-character message: ").strip()
    key = input("Enter 8-character key: ").strip()

    if len(message) != 8 or len(key) != 8:
        print("Error: Both message and key must be exactly 8 characters!")
    else:
        print()
        L1 = get_L1(key, message)
        print("\nFinal L1 =", L1)
