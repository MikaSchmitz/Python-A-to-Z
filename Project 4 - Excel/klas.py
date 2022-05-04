#hier wordt de klass gemaakt

class Persoon():

    #maak een nieuw persoon aan
    def __init__(self, naam, gewicht, leeftijd, woonplaats):
        self.naam = naam
        self.gewicht = gewicht
        self.leeftijd = leeftijd
        self.woonplaats = woonplaats

    def is_jarig(self):
        self.leeftijd = self.leeftijd + 1
        print(f"{self.naam} is nu {self.leeftijd} jaar oud!")