#in dit document worden for loops bekeken

#loop door alle lijst elementen heen
lijst = [1, 2, 3, 4]

for element in lijst:
    print(element)



#loop door letters van een string heen
tekst = "python"
for letter in tekst:
    print(letter)



#een for loop kan ook worden uitgevoerd binnen een for loop
lijst2 = [5, 6, 7, 8]

for element in lijst:
    for ander_element in lijst2:
        print(element, ander_element)



#voorbeeld van een array met meerdere gegevens
gegevens = [
    ("Mika Schmitz", "mika.schmitz@gmail.com", "11"),
    ("Melissa Jagers", "melissajagers@outlook.com", "12")
    ]

for naam, email in gegevens:
    print(f"\n{email}\n\nHallo {naam},\nDit is een test email.")