import requests
import csv
import datetime
import json

class StadtWetter :
    stadt = "Koeln"
    
    tempMorgen = 0;
    
    def __init__(self, text) :
        self.stadt = text
        self.downloadJson()
        
    def downloadJson(self) :
        requestread = requests.get("https://wttr.in/"+self.stadt+"?format=j1")
        file = open("weather"+self.stadt+".json", "w")
        answer = requestread.text
        file.write(answer)
        file.close()
        file2 = open("weather"+self.stadt+".json", "r")
        
        jsonWetter = json.load (file2)
        condition = jsonWetter['current_condition']
        weather = jsonWetter['weather']
        #print(weather[1])
        tomorrow = weather[1]
        hourly = tomorrow['hourly']
        # print(hourly)
        for row in hourly :
            #print(row)
            tempHour = int(row["tempC"])
            print(tempHour)
            if (tempHour > self.tempMorgen) :
                   self.tempMorgen = tempHour
        self.weatherDesc = (condition[0]['weatherDesc'])
           
    
wetterBonn = StadtWetter("Bonn")
print(wetterBonn.weatherDesc)
print(wetterBonn.tempMorgen)
                        
        


