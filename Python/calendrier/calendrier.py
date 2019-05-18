# Titre : Calendrier perpetuel 1
# Role : Déterminé le jour de la semaine
# Entrées : j,m,a : Entrées
# sortie : jour : texte(string)
code = "033614625035"
jour = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

mois = ["JANVIER","FEVRIER","MARS","AVRIL","MAI","JUIN","JUILLET","AOUT","SEPTEMBRE","OCTOBRE","NOVEMBRE","DECEMBRE"]
nombre = [0,31,59,90,120,151,181,212,243,273,304,334]

j = int(input("Jour ? "))
m = str(input("Mois ? "))
a = int(input("Année ? "))
#bissextile = False

valeur = j+nombre[mois.index(m)]

if((a%4==0 and a%100!=0) or (a%400==0)) and mois.index(m)>2:
    valeur=valeur+1

print(valeur)

#si l'année est divisible (et reste un nombre entier) par 4 et non divisible par 100, ou
#si l'année est divisible (et reste un nombre entier) par 400.
"""
if (a%4 >= 0) and (a%100 >= 0) or a%400 >= 0:
    bissextile = True
else:
    bissextile = False




calcul = a%100 + (a%100)//4 + j + int(code[m-1])

numJourAnnee = 0

print("C'était un ", jour[calcul%7])

if bissextile == True:
    print("L'annee est bissextile.")
else:
    print("l'annee n'est pas bissextile.")


if m == 1:
    numJourAnnee = j





janvier = [0,1,2]
fevrier = [0,1,2]

a = 1
if a == 1:
    janvier.append(3)
"""
