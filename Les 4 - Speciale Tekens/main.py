#in dit document worden speciale tekens getoond door middel van escaping ( \ )

#een \n maakt een nieuwe regel
tekst = "\n\nMijn zin"
print(tekst)

#een \t zorgt voor een tab
tekst = "Voorraad \t : \t 12 stuks"
print(tekst)

#een enkele \ zorgt ervoor dat het leesteken erna wordt meegenomen in de string
tekst = "nu kun je de \\t wel zien, dit komt door de extra \\"
print(tekst)

#via de enkele \ kun je dus ook leestekend meenemen
tekst = "Mika zegt: \"Onmogelijk, zou dat echt kunnen?\""
print(tekst)