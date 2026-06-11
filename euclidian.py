a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("\nSteps:")
# gcd = math.gcd(b, a)     -- to get the GCD of two numbers 
# or we can use the Euclidean algorithm as shown below:
while b != 0:

    q = a // b
    r = a % b

    print(a, "=", b, "*", q, "+", r)

    a = b
    b = r

print("\nGCD =", a)