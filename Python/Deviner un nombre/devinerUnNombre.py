import random

randomNumber = random.randint(0,100)
essai = 0

while essai < 10:
    findNumber = int(input("Devinez le nombre : "))

    if findNumber == randomNumber:
        print("Bravo vous avez trouvez le nombre")
        break
    elif findNumber < randomNumber:
        print("Le nombre est plus grand")
    else:
        print("Le nombre est plus petit")

    essai+=1
