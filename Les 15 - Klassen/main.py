#hier wordt een eerste look gegeven aan klassen


#een klasse schrijf je meestal met hoofdletters en zonder spaties
class Persoon():
    
    #een klasse begin met een __init__ functie, hier verklaar je de gegevens van je opject
    def __init__(self, naam, gewicht):
        self.naam = naam
        self.gewicht = gewicht

    #binnen een klasse kun je verschillende functies bouwen om je objecten te weizigen
    #in deze functie laten we een van onze personen eten
    def eet(self):
        self.gewicht = self.gewicht + 1     #gebruik self.gegeven om deze aan te spreken
        print(f"{self.naam} heeft gegeten en is nu {self.gewicht} kilogram.")



#om een object aan te maken doe je dit precies zoals altijd alleen geven we nu de benodigde parameters mee
henk = Persoon("Henk", 75)

#print het object henk uit, dit kan simpelweg door een . te typen gevolgd door het gegeven
print(henk.naam, henk.gewicht,"KG")

#gebruiken we de eet functie komt er +1 op zijn gewicht
henk.eet()
henk.eet()