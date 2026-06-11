
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'ABCDEFGH'      # 8-byte key

cipher = DES.new(key, DES.MODE_ECB)

plaintext = input("Enter Plain Text: ")

encrypted = cipher.encrypt(pad(plaintext.encode(), 8))

print("Encrypted =", encrypted.hex())

decrypted = unpad(cipher.decrypt(encrypted), 8)

print("Decrypted =", decrypted.decode())