p = int(input("Enter Prime Number (p): "))
g = int(input("Enter Primitive Root (g): "))

a = int(input("Enter Alice Private Key: "))
b = int(input("Enter Bob Private Key: "))

A = pow(g, a, p)
B = pow(g, b, p)

KA = pow(B, a, p)
KB = pow(A, b, p)

print("Alice Public Key =", A)
print("Bob Public Key =", B)

print("Alice Secret Key =", KA)
print("Bob Secret Key =", KB)