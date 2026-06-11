import math

n = int(input("Enter Number: "))

count = 0

for i in range(1, n + 1):
    if math.gcd(i, n) == 1:
        count += 1

print("Euler Totient φ(", n, ") =", count)
