def cal(j,m,a) :
    Tab = [0,31,59,90,120,151,181,212,243,273,304,334]
    valeur=j+Tab[m-1]

    if ((a%4==0 and a%100!=0) or (a%400==0)) and m>1:
        valeur=valeur+1
    return valeur

j1 = int(input("Entrer un jours :"))
m1 = int(input("Entrer un mois :"))
a1 = int(input("Entrer une année :"))

j2 = int(input("Entrer un autre jours :"))
m2= int(input("Entrer un autre mois :"))
a2 = int(input("Entrer une autre année :"))

nb1=cal(j1,m1,a1)
nb2=cal(j2,m2,a2)

if m1<m2 :
    annees=(a2-a1)*365
elif m1>m2:
    annees=(a2-a1-1)*365
else:
    if (j1>j2):
        annees=(a2-a1-1)*365
    else:
        annees=(a2-a1)*365

for a in range(a1,a2):
    if ((a%4==0 and a%100!=0) or (a%400==0)) :
        annees+=1

if nb2>nb1 :
    valeur=nb2-nb1+annees
else :
    valeur=nb2-nb1+annees+365
print (valeur)
