from random import randint

score = [0,0]
joueur = 0
j = "joueur 1"

while score[0] != 50 or score[1] != 50:
    print("Score ", j, " : " , score[joueur])
    print("\nTour de ", j)
    n = int(input("nombres de des ? "))

    for i in range(n):
        d = randint(1,6)
        print("\nde :", i+1, "valeur : ", d)
        score[joueur] = score[joueur] + d
    print("\nScore ", j, " : " , score[joueur])
    if joueur == 0:
        j = "Joueur 2"
        joueur = 1
    else:
        j = "joueur 1"
        joueur = 0

    if score[0] > 50:
        score[0] = 35
        print("Redescend à 35")

    if score[0] == 50:
        print("Joueur 1 gagne !")
        break
    elif score[1] == 50:
        print("Joueur 2 gagne !")
        break









"""
def game():
    nbLanceDeJ1 = int(input("Joueur 1 : Combien de fois voulez vous lancez les dés ? (1, 2 ou 3) "))
    nbLanceDeJ2 = int(input("Joueur 2 : Combien de fous voulez vous lancez les dés ? (1, 2 ou 3) "))

    de = random.randint(1, 6)
    nbLance = nbLanceDeJ1+nbLanceDeJ2


    while joue:
        de = random.randint(1,6)
        score = nbLance * de
        n+=1
        print("Score = ", score)

        if score == 50:
            print("Gagne")
        elif score > 50:
            print("Score = ", score)
            score = 35


def somme(nombreDes):
    s = 0
    for i in range(0, nombreDes):
        s = s+random.randint(1,6)
    return s

score1 = 0
score2 = 0
joueur1 = True
"""












tab = [[1, 2, 3], [4, 5, 6]]
print(tab)
