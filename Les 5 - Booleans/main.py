#in dit document wordt gekeken naar booleans (true / false)

#deze variablen hebben nu waardes
a = 1
b = 2
c = 1

#check of de vergelijking klopt en toont het antwoord
print(a < b)    #   < is kleiner dan

print(a > b)    #   < is groter dan

print(a <= c)    #   <= is kleiner dan of gelijk aan

print(a >= b)    #   <= is groter dan of gelijk aan

print(a == b)   #   == is gelijk aan

print(a != c)   #   != is niet gelijk aan

print((a < b) & (b > c))





#voorgaande lessen komen hier terug, we laten een string zien en nemen de variabelen mee in de tekst via de format functie, na de comma komt de daadwerkelijke berekening
print(f"{a} is kleiner dan {b}", a < b)