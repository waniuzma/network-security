def encrypt(text, rails):
    fence = ['' for _ in range(rails)]

    row = 0
    direction = 1

    for ch in text:
        fence[row] += ch

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return ''.join(fence)


def decrypt(cipher, rails):
    n = len(cipher)

    pattern = [['' for _ in range(n)] for _ in range(rails)]

    row = 0
    direction = 1

    for col in range(n):
        pattern[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    index = 0

    for i in range(rails):
        for j in range(n):
            if pattern[i][j] == '*':
                pattern[i][j] = cipher[index]
                index += 1

    result = ""

    row = 0
    direction = 1

    for col in range(n):
        result += pattern[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return result


text = input("Enter Plain Text: ").upper()
rails = int(input("Enter Rails: "))

cipher = encrypt(text, rails)
plain = decrypt(cipher, rails)

print("Encrypted Text =", cipher)
print("Decrypted Text =", plain)