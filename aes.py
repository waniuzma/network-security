from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'   # 16 bytes key

cipher = AES.new(key, AES.MODE_ECB)

plaintext = input("Enter Plain Text: ")

encrypted = cipher.encrypt(pad(plaintext.encode(), 16))

print("Encrypted =", encrypted.hex())

decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Decrypted =", decrypted.decode())

