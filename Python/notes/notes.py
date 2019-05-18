from statistics import mean

nbrNotes = int(input("Combiens de notes ? "))
notes = []
temp = 0

for i in range(nbrNotes):
    print("Notes n° ", i)
    notes.append(int(input()))

for i in range(len(notes)):
    for j in range(len(notes)-1):
        if notes[j] > notes[j+1]:
            temp = notes[j]
            notes[j] = notes[j+1]
            notes[j+1] = temp

print("La note la plus basse est ", notes[0],"/20")
print("La note la plus haute est ", notes[-1],"/20")
print("La moyenne est ", round(mean(notes), 2), "/20")