a = int(input("a = "))
b = int(input("b = "))

while b!=0:
    c = a % b
    a = b
    b = c
    d = a*b
    d = d/a

    print("a = ", a, " b = ", b, " c = ", c)
    print("PPCM = ", d)

print("PGCD = ", a)
