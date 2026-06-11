a = int(input("Enter a: "))
p = int(input("Enter Prime Number p: "))

result = pow(a, p - 1, p)

print("a^(p-1) mod p =", result)

if result == 1:
    print("Fermat's Theorem Verified")
else:
    print("Not Verified")