import random
geheimcode = [random.randrange(9), random.randrange(9), random.randrange(9), random.randrange(9)]
print(geheimcode)
erraten = False
while not (erraten) :
    tipp = [int(input ('Tipp Ziffer 1 ') ), int(input ('Tipp Ziffer 2 ') ), int(input ('Tipp Ziffer 3 ') ), int(input ('Tipp Ziffer 4 ') )]
    anzahlgenaurichtig = 0;
    anzahlanandererstelle = 0;
    schongetippt = dict(zip(geheimcode, [0, 0, 0, 0]))
    print ("Schon getippt: ", schongetippt)
    
    for i in range(4) :
        print ("Schon getippt: ", schongetippt)
        if (geheimcode[i] == tipp[i]) :
            anzahlgenaurichtig += 1
            schongetippt[tipp[i]]+= 1
        else :
            if (tipp[i] in geheimcode and schongetippt[tipp[i]] < geheimcode.count(tipp[i])) :
                anzahlanandererstelle += 1
        
    if (anzahlgenaurichtig == 4) :
           break
    print("Anzahl Genau Richtig", anzahlgenaurichtig)
    print("Anzahl an anderer Stelle", anzahlanandererstelle)

          
