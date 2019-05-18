def pascal(index):
    tab = [1, 1]

    for i in range(2, index-2):
        tab.append(tab[i] + tab[i+1])

    print(tab)
    # premier(tab)


index = int(input("Combien de terme ? : "))
pascal(index)
