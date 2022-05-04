#hier gaan we afbeeldingen bewerken
#hiervoor is de extentie 'pillow' nodig, deze kan worden gedownload met ---> python -m pip install pillow

#soms is de actieve directory anders dan gewenst, wanneer dit zo is weizig deze dan via de os.chdir() command, dit is zeker niet altijd zo

#verander de directory naar de huidige dir
import os                  
os.chdir(os.path.dirname(__file__))
#import image editor from pillow
from PIL import Image

#haal de naam van elke afbeelding op
afbeeldingen = os.listdir("afbeeldingen")

#doe onderstaande functies voor iedere foto
for afbeelding_naam in afbeeldingen:

    #haal afbeelding op, gebruik os.path.join zodat die op elke OS werkt
    afbeelding = Image.open(os.path.join("afbeeldingen", afbeelding_naam))

    #gebruik de vorige afbeelding om een nieuwe zwart witte te maken
    afbeelding_zwart_wit = afbeelding.convert("L")
    #maak een thumbnail van de afbeelding door middel van afmetingen
    afbeelding_zwart_wit.thumbnail((256, 256))
    #sla de bewerkte afbeeldingen op in een andere map (weer via os.join)
    try:
        afbeelding_zwart_wit.save(os.path.join("Bewerkte Afbeeldingen", afbeelding_naam))
        print(f"Bewerking {afbeelding_naam} succesvol afgerond.")
    except:
        print(f"Bewerking {afbeelding_naam} is gefaald.")
    
