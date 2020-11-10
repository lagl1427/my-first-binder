import requests
import csv
import datetime


#requestread = requests.get("https://stadtplan.bonn.de/csv?OD=4379")
#file = open("covid19-data.csv", "w")
#file.write(requestread.text)
#file.close()
file2 = open("covid.csv", newline='')
csvinhalt =csv.reader(file2, delimiter=';')
sortedlist = sorted(csvinhalt, key=lambda row: row[0], reverse=True)
#print(sortedlist)

fallzahlmin = int(input("Anzeigen größer als:"))
#print(csvinhalt)
maxdate = None
fallzahlmax = 0
for row in sortedlist :
    
    try :
        fallzahl = int(row[2])
        if (fallzahl > fallzahlmin) :
            if (fallzahl > fallzahlmax) :
                fallzahlmax = fallzahl
                maxdate = (row[0])
                print(row)
    except:
        print(row)
print(maxdate)
print(fallzahlmax)