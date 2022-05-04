#het maken en oproepen van functies


#met def maken we een functie, gevolgd door de naam om de functie aan te roepen
#achter de naam zetten we haakjes voor parameters en een dubbele punt
def vraag_gebruiker_naar_naam():
    naam = input("Wat is je naam? ")
    print(f"De naam {naam} bestaat uit", len(naam), "tekens")

#type de naam van de functie gevolgd door haakjes (met mogelijke parameters) om de functie op te roepen
vraag_gebruiker_naar_naam()







#hier wordt gebraagd voor een parameter
def kwadraat(getal):
    het_kwadraat = getal ** 2   #het kwadraat van het gevraagde getal wordt berekend
    return het_kwadraat         #haal het eind resultaat op voor gebruik buiten de functie

#print de functie, de parameter is hier 4
print(kwadraat(4))







#maak een functie met 2 parameters
def verminigvuldig(getal_links, getal_rechts):
    vermenigvuldiging = getal_links * getal_rechts  #getal links keer getal rechts
    return vermenigvuldiging

#x is de uitkomst van de functie, dit is een van vele manieren om een functie op te roepen
x = verminigvuldig(12, 7)
print(x)