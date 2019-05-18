"""
A = int(input("Rentrez un nombre : "))
B = A

if A % 2 == 1:
    print("Votre nombre est impaire")
    B = A-1

print("Le plus grand entier pair inféerieur à ", A, "est : ", B)


n = 65

while (n <= 90):
    print(chr(n))
    n+=1
          
"""

for i in range(2, 11):
    print("table de ", i)
    for j in range(1, 11):
        print(i, " x ", j ," = ", i*j)
