
def teilbarDurch2(zahl) :
    if (zahl > 1) :
        return teilbarDurch2(zahl -2)
    elif zahl == 1 :
        return False
    else :
        return True
            
zahl = int(input("Zahl: "))
print("Gerade: ", teilbarDurch2(zahl))