#Titre : Jeu pourri 2
#Role : Calendrier
# Entrer : jj,mm : entier
# Sortie : Text : string

j = 1
m = 1

joueur1 = True
mois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while (j != 31 and m != 12):
    if joueur1 == True:
        print("Joueur 1 : ")
        joueur1 = False
    else:
        print("Joueur 2 : ")
        joueur1 = True

    jj = int(input("Jour : "))
    mm = int(input("Mois : "))

    if jj > mois[mm-1] or (jj != j and mm != m) or (jj == j and mm == m):
        print("Perdu")
        break
    else:
        j = jj
        m = mm

if j == 31 and m == 12:
    print("GAGNE")
