
def bubblesort(liste) :
    unsortiert = True
    while unsortiert :
        unsortiert = False
        for i in range(len(liste)-1) :
            if liste[i] < liste[i+1] :
                unsortiert = True
                tmp = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = tmp
                print(liste)
        print("New Durchlauf", liste)
    return liste    

print("Liste: ", bubblesort([int(input("Wert")),int(input("Wert")),int(input("Wert")),int(input("Wert")),int(input("Wert")),int(input("Wert"))]))