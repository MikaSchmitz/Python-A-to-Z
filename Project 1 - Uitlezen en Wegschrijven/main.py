#in dit project moet data van een tekstbestand kunnen worden weggschreven en opgehaald.


#soms is de actieve directory anders dan gewenst, wanneer dit zo is weizig deze dan via de os.chdir() command, dit is zeker niet altijd zo
#verander de directory naar de huidige dir
import os                   
os.chdir(os.path.dirname(__file__))  




#een lijst met alle mogelijke opties voor het tekstbestand
opties = ["r", "a", "w"]
#start een oneindige loop            
while True:
    #vraag de gebruiker wat hij wilt doen in de vorm van een int
    keuze = int(input("Wat wilt u met het bestand doen? [0] lezen, [1] toevoegen, [2] nieuw bestand, [3] verwijderen: "))  

    #vraag de naam van het bestand
    bestandNaam = input("Wat is de naam van het bestand? ")
    if bestandNaam == "":
        bestandNaam = "kladblok"

    #haal een bestand op als de gevraagde functie
    if keuze != 3:
        bestand = open(file=f'{bestandNaam}.txt', mode=opties[keuze])            


    #wanneer 0 wordt gekozen kan het bestand worden bewerkt
    if keuze == 0:
        for regel in bestand:
            #laat iedere regel zien als string en haal onnodige leestekens weg
            print(regel.strip())


    #wanneer de keuze 1 is kan er text worden toegevoegd
    elif keuze == 1:
        #vraag input aan de gebruiker
        toevoeging = input("Wat wilt u schrijven? ")
        #voeg de regel toe via een if statement
        if bestand.write(f"\n{toevoeging}"):
            print("Regel toegevoegd")
        else:
            print("Toevoegen mislukt")


    #wanneer de keuze 2 is wordt er een nieuwe bestand gemaakt, in dit geval wordt de oude dus overschreven
    elif keuze == 2:
        #vraag input aan de gebruiker
        toevoeging = input("Wat wilt u schrijven? ")
        #voeg de regel toe via een if statement
        if bestand.write(toevoeging):
            print("Nieuw bestand gemaakt")
        else:
            print("Error")


    elif keuze == 3:
        os.remove(f"{bestandNaam}.txt")
        print(f"{bestandNaam}.txt is verwijderd")


    #wanneer de keuze afwijkt van de opties wordt de vraag nog eens gesteld
    else:
        continue

    
    #sluit bestand
    if keuze != 3:
        bestand.close()
    
