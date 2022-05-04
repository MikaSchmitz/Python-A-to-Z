#In dit document worden basis operators en vairabelen uitgelegd

a = 123 + 123   #     + telt de gegevens bij elkaar op

b = 123 - 123   #     - trekt de gegevens van elkaar af

c = 4 * 2       #         * vermenigvuldigt getallen

d = 4 / 2       #         / deelt de getallen tot na de comma

e = 4 // 2      #        // deelt de getallen tot aan de comma

f = 2 ** 3      #        ** vermenigvuldigt het eerste getal tot de macht van het tweede getal

g = 7 % 2       #         % laat zien hoeveel je overhoud wanneer je het eerste getal maximaal deelt door het tweede

h = 2 ** 3      #         je kunt een uitkomt opslaan als variabel
i = 17          #         ook kun je direct de waarde meegeven aan de variabel
j = i - h       #         dit wilt ook zeggen dat je de (berekende) variabel later weer kunt gebruiken, hier bereken je bijvoorbeeld 17 - 8 (omdat 2 ** 3 = 8)

#onderstaande functie laat de uitkomst van een van de voorgaande variabelen zien, verander de a op regel 26 door de gewenste variabel
def show(example):
    print(example)

#laat uitkomst zien
show(a)