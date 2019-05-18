# Titre    :  Syracuse
# Rôle     :  Donner la suite
# Entrée   :  n : entier
# Sortie   :  tab : tableau à l'admission

# n = int(input("Choisir un nombre n : "));
#
# while n != 1:
#     if n % 2 > 0:
#         n = n * 3 + 1
#     else:
#         n = n / 2
#
#     print(round(n))


tv = int(input("Temps de vol : "))
tabTv = []
tabnb = []

for number in range(2, 2**tv+1):
    tabnb.append(number)
    tab = [number]
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1

        tab.append(int(number))
    tabTv.append(len(tab)-1)
print(tabnb)
print(tabTv)
for i in range(0, len(tabTv)):
    if tabTv[i] == tv:
        print(tabnb[i])


# def syracuse(number):
#     while number != 1:
#         if number % 2 == 0:
#             number = number / 2
#         else:
#             number = 3 * number + 1
#
#         tab.append(int(n))
#
#
# n = int(input("Nombre ? "))
# tv = int(input("Temps de vol : "))
# nbr = n
# tab = [n]
#
# syracuse(n)

# somme = sum(tab)
# print(tab)
# print("Somme = ", somme)
# print("Temps de vol = ", len(tab)-1)
# print("Somme / temps de vol = ", somme / len(tab)-1)
# print("Somme / n = ", somme / nbr)
