class Geburtstag :
    tt = 0
    mm = 0
    jjjj = 0
    
    def __init__(self, tag, monat, jahr) :
        self.tt = tag
        self.mm = monat
        self.jjjj = jahr
    
    def printGeburtstag(self) :
        print(self.tt, '.', self.mm, ".", self.jjjj)


geburtstag = Geburtstag(18, 1, 1975)
geburtstag.printGeburtstag()