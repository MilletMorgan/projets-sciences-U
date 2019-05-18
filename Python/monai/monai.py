from tkinter import *

def calcul_rendu():
        #output.delete(0.0, END)

        monai = [1, 2, 5, 10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
        euro = ["1 centime", "2 centimes", "5 centimes", "10 centimes", "50 centimes", "1€", "2€", "5€", "10€", "20€",
                "50€", "100€", "200€", "500€"]
        piece = []
        monai.reverse()
        euro.reverse()
        get_prix = prix.get()
        int_prix = float(get_prix)
        get_paiement = paiement.get()
        int_paiement = float(get_paiement)
        rendu = int_prix - int_paiement
        rendu = round(rendu, 2)
        euroToCtm = rendu * 100
        rendu_list = Listbox(window, width=30)

        output.insert(END, rendu)

        for i in range(len(monai)):
                for j in range(len(monai) - 1):
                        if euroToCtm // monai[j]:
                                euroToCtm = euroToCtm - monai[j]
                                piece.append(euro[j])

        for i in range(len(piece)):
                nbr = piece.count(piece[i])
                rendu_list.insert(END, str(nbr) + ' pièce/billets de ' + str(piece[i]))
                rendu_list.grid(sticky=W)

window = Tk()
window.title("Rendons la monais de sa pièce")
window.configure(background="#303030")

Label(window, text="Prix : ", background="#303030", fg="#FFF").grid(row=1, column=0, sticky=W)
prix = Entry(window, width=30)
prix.grid(row=2, column=0, sticky=W)

Label(window, text="Paiement : ", background="#303030", fg="#FFF").grid(row=3, column=0, sticky=W)
paiement = Entry(window, width=30)
paiement.grid(row=4, column=0, sticky=W)

Button(window, text="Calculer le rendu", width=15, command=calcul_rendu).grid(row=5, column=0)

Label(window, text="Rendu : ", background="#303030", fg="#FFF").grid(row=6, column=0, sticky=W)
output = Text(window, background="#FFF", width=30, height=1, wrap=WORD)
output.grid(row=7, column=0, columnspan=2, sticky=W)

window.mainloop()

""""
prix = float(input("Prix : "))
paiement = float(input("Paiement : "))

"""
