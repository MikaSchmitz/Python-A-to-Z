#een kijkje naar breaks en het hervatten ervan

lijst = [1, 2, 3, 4, 5]

#in onderstaande loop wordt een break gebruikt, dit breekt de loop en laat de code erbuiten verder gaan
for getal in lijst:
    print(getal)

    if getal == 3:
        break   #beeindig loop

print("eind for.")



#hier wordt continue gebruikt, dit laat de loop direct terug gaan naar het begin en negeert de rest van de code
for getal in lijst:
    if getal == 3:
        continue    #ga terug naar begin
    print(getal)

print("eind for.")



som = 0

while som < 10:
    som = som + 1
    print(som)

    if som == 5:
        break   #beeindig loop

print("eind while")



while som < 10:
    som = som + 1

    if som == 9:
        continue    #ga terug naar begin

    print(som)

print("eind while")