from Crypto.Cipher import ARC4

key = b"SECRETKEY"

cipher = ARC4.new(key)

plaintext = input("Enter Plain Text: ")

encrypted = cipher.encrypt(plaintext.encode())

print("Encrypted =", encrypted.hex())

cipher = ARC4.new(key)

decrypted = cipher.decrypt(encrypted)

print("Decrypted =", decrypted.decode())