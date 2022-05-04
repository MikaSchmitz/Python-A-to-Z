#hier zie je de basis van een dictionary

woordenboek = {
    "bedrijf"   : "Mika inc.",
    "werknemers": [
        "Mika",
        "Ruben",
        "Melissa"
    ]
}

#vraag een begrip binnen het woordenboek op, gebruik de index om te specificeren welke
print(woordenboek["bedrijf"],  "Werknemer:", woordenboek["werknemers"][0])