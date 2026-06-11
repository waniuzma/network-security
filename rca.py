p = int(input("Enter p: "))
q = int(input("Enter q: "))
e = int(input("Enter e: "))
M = int(input("Enter Message: "))

n = p * q
phi = (p - 1) * (q - 1)

# Find d
for d in range(1, phi):
    if (e * d) % phi == 1:
        break

# Encryption
C = pow(M, e, n)

# Decryption
P = pow(C, d, n)

print("Public Key =", (e, n))
print("Private Key =", (d, n))

print("Encrypted =", C)
print("Decrypted =", P)