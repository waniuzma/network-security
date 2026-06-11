a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

r1 = a
r2 = b

s1 = 1
s2 = 0

t1 = 0
t2 = 1

print("\nq\t r1\t r2\t s1\t s2\t t1\t t2")

while r2 != 0:

    q = r1 // r2

    print(q,"\t",r1,"\t",r2,"\t",s1,"\t",s2,"\t",t1,"\t",t2)

    r = r1 - q*r2
    r1 = r2
    r2 = r

    s = s1 - q*s2
    s1 = s2
    s2 = s

    t = t1 - q*t2
    t1 = t2
    t2 = t

print("\nGCD =", r1)
print("x =", s1)
print("y =", t1)

print("Verification =", a*s1 + b*t1)