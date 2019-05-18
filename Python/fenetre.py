from tkinter import *
from functools import partial
from statistics import mean

notes = []
temp = 0

def Verification():
    nombresNotes = int(nbrNotes.get())

    for i in range(int(nbrNotes.get())):
        note = Entry(root)
        note.focus_set()
        note.pack(side = LEFT, padx = 5, pady = 5)
        notes.append(note.get())

    button = Button(root, text ='Valider', command = triABulle)
    button.pack(side = LEFT, padx = 5, pady = 5)
    
def triABulle():
    for i in range(len((notes))):
        for j in range(len(notes)-1):
            if notes[j] > notes[j+1]:
                temp = notes[j]
                notes[j] = notes[j+1]
                notes[j+1] = temp
    
    label2 = Label(root, text = "La note la plus basse est ")
    label2.pack(side = LEFT, padx = 5, pady = 5)

    note0 = notes[0]
    sample = Label(root, text = note0)
    sample.pack()

root = Tk()
root.title('Moyenne')

Label1 = Label(root, text = 'Combiens de notes ? ')
Label1.pack(side = LEFT, padx = 5, pady = 5)

nbrNotes = Entry(root)

nbrNotes.focus_set()
nbrNotes.pack(side = LEFT, padx = 5, pady = 5)

Bouton = Button(root, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)

root.mainloop()