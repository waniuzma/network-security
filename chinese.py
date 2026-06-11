n = int(input("Enter Number of Equations: "))

a = []
m = []

for i in range(n):

    r = int(input("Enter Remainder: "))
    mod = int(input("Enter Modulus: "))

    a.append(r)
    m.append(mod)

M = 1

for mod in m:
    M *= mod

x = 0

for i in range(n):

    Mi = M // m[i]

    yi = 1

    while (Mi * yi) % m[i] != 1:
        
        yi += 1

    x += a[i] * Mi * yi

print("Solution =", x % M)