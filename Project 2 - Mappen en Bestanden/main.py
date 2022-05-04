#hier wordt gekeken naar navigatie tussen mappen en bestanden

#soms is de actieve directory anders dan gewenst, wanneer dit zo is weizig deze dan via de os.chdir() command, dit is zeker niet altijd zo
#verander de directory naar de huidige dir
import os                  
os.chdir(os.path.dirname(__file__))

#zet het huidige pad om in een string
huidig_pad = os.getcwd()

#laat dit bestand deelnemen aan het project
tekstbestand_pad = os.path.join(huidig_pad, "tekstbestanden", "tekstbestand.txt")

#het tekstbestand staat in een andere map, gebruik de volledige route om deze te vinden
tekstbestand = open(tekstbestand_pad, "r")
print(tekstbestand.readlines())



#toon alle bestanden in het gevraagde pad
print(os.listdir())



#importeer een ander bestand (imported.py)
import imported
#roep een functie uit een ander bestand
imported.alert()