#ready to play
import time
import random

#print("Welcome to Narvalia.")
#time.sleep(2)
#print("")
#print("The story of this great place is one that has been lost through the ages.")
#time.sleep(3)
#print("")
#print("Forgotten by all but my family.")
#time.sleep(2)
#print("")
#print("My family is a line of powerful mages that evaded the king's soldiers at almost every turn.")
#time.sleep(4)
#print("")
#print("So let me tell you the story of an acient time, one of magic, poverty, racism, and an all around awful situation.")
#time.sleep(6)
#print("")
#print("Ahem")
#time.sleep(1)
#print("")
#print("Once apon a time, Narvalia was a beautiful place.")
#time.sleep(3)
#print("")
#print("Until that is a mystical event took place that would change the world.")
#time.sleep(3)
#print("")
#print("An event that would cause the greatest advances and the worst conflicts.")
#time.sleep(4)
#print("")
#print("After a long night of rest you wake up")
#time.sleep(3)

###Game begins here###

name=input("Enter your name or enter random: ")
namel=name.lower()
if namel=="random":
    names=["Winerah", "Arcake", "Anjeff", "Savid", "Brito", "Gormamen", "Lin", "Gakim", "Thasevermark", "Riwyn", "Ingchar", "Ordlett", "Markdino", "Thaechet", "Garlas", "Beth", "Winemax", "Nidic", "Donni", "Laubrandca",]
    AIchoice=random.randint(0,19)
    name=names[AIchoice]
    print(name)
else:
    print("Hello "+name)
    
