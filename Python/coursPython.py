def myFunc(): #Fonction
    a = 5

b = 4 #Variable Int : Uniquement des nombres sans virgule, positif et négatif.
c = 1.5 #Variable Double : Nombre avec et sans virgule, positif et negatif.
d = "Hello Word!" #Variable alphanumérique
e = True #Boolean Vrai
f = False #Boolean Faux

resultat = a - b #calcul

print("Bonjour") #Afficher un message.
print(c) #Affiche le contenue d'une variable, ici 1.5.
print("a - b = ", resultat) #Les deux combinés

# Structure conditionnel (==, ===, <, >, <=, >=, !=)
if a == 5:
    print("a est egal a 5")
elif a > 5:
    print("a est supperieur à 5")
else:
    print("a est inférieur à 5")

#Bouvle

n = 0

while n != 10: #Affiche de 0 à 9
    print("n = ", n)
    n+=1

for i in range(5,10): #Affiche de 5 à 9
    print(i)

#Tableau

tableau = [1, 2, 3] #Case 0, 1 et 2
print(tableau[1]) #Affiche le nombre 2
