#hier wordt er iets meer uitlegd over het uitpakken van tuples

mijn_tuple = (1, 2, 3)

#een tuple kan worden verdeelt over meerdere variabelen
x, y, z = mijn_tuple

print(x)

#een lijst kan ook bestaan uit tuples
lijst = [(1, 2), (3, 4), (5, 6)]

#laat elke tuple in de lijst zien
for x, y in lijst:
    print("lijst:", x)