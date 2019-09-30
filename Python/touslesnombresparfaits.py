def nbrPremier():
    borne = int(input("Borne : "))

    tab = []

    for nombre in range(1, borne + 1):
        s = 0
        for i in range(1, nombre):
            if nombre % i == 0:
                s = s + i
        if s == nombre:
            tab.append(s)

    print("Les nombres parfait jusqu'a", borne, "sont : ", tab)


nbrPremier()


def sommediviseur(n):
    s = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            s = s + i
    return s

def abondant():

    borne = int(input("Borne : "))

    tab = []

    for nombre in range(1, borne + 1):
        if sommediviseur(nombre) > nombre:
            tab.append(nombre)
            print("Est abondant")
        else:
            print("n'est pas abondant")

    print("densite jusqu'a ", borne, " : ", len(tab)/borne)
    print(tab)

abondant()