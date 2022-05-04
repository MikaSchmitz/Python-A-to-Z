#in dit document wordt de basis van een string getoond

#dubbele aanhalingstekens
naam = "Mika"
print(naam)



#enkel aanhalingsteken
achternaam = 'Schmitz'
print(achternaam)


#een string kan worden samengesteld uit verschillende andere variabelen
volledigeNaam = naam + " " + achternaam
print(volledigeNaam)



#escaping, neem een aanhalingsteken mee in de string door middel van een backslash
escaping = "Mika\'s appel"
print(escaping)



#een string opvragen, opslaan en teruglezen
invoernaam = input("Wat is uw naam? ")
print("(Simpele versie) Hallo, " + invoernaam)



#format de invoer naam in de string via de oude methode
groet = "Hallo, {}".format(invoernaam)
print("(Oud format) " + groet)



#format de invoer naam in de string via de nieuwe methode
groet_nieuw = f"Hallo, {invoernaam}"
print("(Nieuw format) " + groet_nieuw)