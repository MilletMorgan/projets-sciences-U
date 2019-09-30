nombre = int(input("Donner un nombre : "))
s = 0

for i in range(1, nombre):
    if nombre % i == 0:
        s = s + i

if s == nombre:
    print(nombre, " est parfait.")
else:
    print(nombre, " n'est pas parfait.")
