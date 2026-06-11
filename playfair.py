def generate_matrix(key):
    key = key.upper().replace("J", "I")

    matrix = []
    used = ""

    for ch in key:
        if ch not in used and ch.isalpha():
            used += ch

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch not in used:
            used += ch

    for i in range(0, 25, 5):
        matrix.append(list(used[i:i+5]))

    return matrix


def find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def encrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        return matrix[r1][(c1+1)%5] + matrix[r2][(c2+1)%5]

    elif c1 == c2:
        return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c2]

    else:
        return matrix[r1][c2] + matrix[r2][c1]


def decrypt_pair(matrix, a, b):
    r1, c1 = find_pos(matrix, a)
    r2, c2 = find_pos(matrix, b)

    if r1 == r2:
        return matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]

    elif c1 == c2:
        return matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]

    else:
        return matrix[r1][c2] + matrix[r2][c1]


key = input("Enter Key: ").upper()
text = input("Enter Plain Text: ").upper().replace("J","I")

if len(text) % 2 != 0:
    text += "X"

matrix = generate_matrix(key)

cipher = ""

for i in range(0, len(text), 2):
    cipher += encrypt_pair(matrix, text[i], text[i+1])

print("Encrypted Text =", cipher)

plain = ""

for i in range(0, len(cipher), 2):
    plain += decrypt_pair(matrix, cipher[i], cipher[i+1])

print("\nDecryption:")
print("Decrypted Text =", plain)