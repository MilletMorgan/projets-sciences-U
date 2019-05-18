import random

"""
def revision():
    n = 0
    result = 0
    table = int(input("Quel table souhaite tu révisé ? "))

    for n in range(11):
        print(table, " x ", n, " = ", result)
        n+=1
        result = table*n

    print("\n")
    main()
"""

def revision():
    for i in range(2, 11):
        print("Table de ", i)
        for j in range(1, 11):
            print(i, " x ", j, " = ", i*j)

def calcul():
    score = 0
    question = 0

    while question < 11:
        a = random.randint(1,9)
        b = random.randint(1,9)
        result = a*b
        resultUser = 0

        #while resultUser != result:
        print("Question ", question, ", combien font ",a," x ",b," ? ")
        resultUser = int(input())

        if resultUser != result:
            print("Faux, résultat : ", result, ".\n")
        else:
            print("Bravo")
            score+=1
        question+=1

    print("Note : ", score, "/10")

def main():
    reviser = int(input('Veux tu révisé ? oui (1) / non (0) : '))

    revision() if reviser == 1 else calcul()

main()
