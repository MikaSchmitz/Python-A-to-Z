#hier wordt gekeken naar lists, Tuples en Sets

#een list wordt opgebouwd tussen brackets
lijst = [1, 2.0, "drie"]

print(lijst[0])     #haal een element uit de lijst op
print(len(lijst))   #wat is de lengte van de lijst

lijst.append(4)     #voeg iets toe aan de lijst   

print(lijst[-1])    #haal het laatste element uit de lijst op


print(lijst[0:2])   #geef aan TOT aan welk element je lijst wilt bekijken (niet tot en met)

print(lijst[1:])    #begin bij element 1

print(lijst[:2])    #stop bij element 2




#[begin:eind:stappen]
grotere_lijst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(grotere_lijst[0:7:2])     #begin bij 0 en stop bij element 7 in stappen van 2
print(grotere_lijst[0::3])      #begin bij 0 in stappen van 3
print(grotere_lijst[::-1])      #toon lijst in omgekeerde volgorde




lijst[0] = "iets nieuws"    #verander een element
print(lijst)



#tupel is een lijst die niet geweizigd kan worden
een_tuple = (1, 2, "Mika")



#in een set kan een element maar een keer voorkomen
een_set = {1, 2, 3, 1, 2, 1}
een_set.add(4)      #voeg toe aan de set

verzameling = set(lijst) #maak een set uit een lijst