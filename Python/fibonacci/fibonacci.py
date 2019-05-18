from math import *

# Titre : Suite de Fibonacci
# Rôle : Déterminer la suite
# Entrée : index : entier
# Sortie : tab : Tableau à 1 dimension


# def fibonacci(index):
#     if index < 0:
#         return -1
#     if index == 0:
#         return 0
#     if index == 1:
#         return 1
#     else:
#         return fibonacci(index - 1) + fibonacci(index - 2)
#
#
# print(fibonacci(8))
#
#
# def fibonacci(index):
#     i = 0
#     j = 1
#     for k in range(index):
#         temp = i + j
#         i = j
#         j = temp
#
#         print(i)
#
#
# index = int(input("Votre nombre : "))
# fibonacci(index)
#
# index = int(input("Combien de terme ? : "))
#
# i = 0
# j = 1
#
# for k in range(index):
#     temp = i + j
#     i = j
#     j = temp
#
#     print(i)


# def premier(tab):
#     #if (not(type(n) is int)) :
#     #   raise ValueError("n doit etre un entier")
#     for i in tab:
#         if tab[i] <= 1 :
#             print(tab[i], " n'est pas premier")
#         for j in range(2, tab) :
#             if tab[i] % j == 0:
#                 print(tab[i], " n'est pas premier")
#         print(tab[i], " est premier")
#
#
#     print(premier(10))


def fibonacci(index):
    tab = [1, 1]
    tab2 = [1]

    for i in range(2, index):
        tab.append(tab[i-1] + tab[i-2])
        #tab2.append(tab[i-1]/tab[i-2])

    print(log(tab[index-1])+1)
    #print(tab2)
    # premier(tab)

index = int(input("Combien de terme ? : "))
fibonacci(index)