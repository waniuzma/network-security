import numpy as np

key = np.array([[3,3],
                [2,5]])

text = input("Enter Plain Text (2 letters): ").upper()

P = np.array([[ord(text[0])-65],
              [ord(text[1])-65]])

C = np.dot(key, P) % 26

cipher = ""

for i in range(2):
    cipher += chr(C[i][0] + 65)

print("Encrypted Text =", cipher)

# Inverse matrix for [[3,3],[2,5]]
inverse_key = np.array([[15,17],
                        [20,9]])

P2 = np.dot(inverse_key, C) % 26

plain = ""

for i in range(2):
    plain += chr(P2[i][0] + 65)
print("\nDecryption:")
print("Decrypted Text =", plain)