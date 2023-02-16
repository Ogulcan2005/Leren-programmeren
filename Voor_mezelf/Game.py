print("Je wordt wakker en je moet naar school.")
opstaan = input("(1)Ga je vandaag naar school of (2)meld je zelf ziek?")
if opstaan == "1":
        print("Je loopt naar de douche.")
        douchevraag= input("Ga je vandaag douchen? (ja/nee)").lower()
        if douchevraag == "ja":
            shampoovraag = input("Ga je shampoo gebruiken. (ja/nee)").lower()
            if shampoovraag == "ja":
                print("Je gaat vandaag lekker ruiken.")
            elif shampoovraag == "nee":
                print("je gaat vandaag niet fris ruiken.")
        elif douchevraag == "nee":
            print("Gadverdamme je gaat ruiken naar een dode kat.")
        tandenpoesten = input("Ga jij je tandenpoetsen? (ja/nee)").lower()
        if tandenpoesten == "ja":
            print("je adem ruikt vandaag fris.")
        elif tandenpoesten == "nee":
            print("Je adem gaat vandaag ruiken naar bedorven ei.")
        kleding = int(input("Je gaat je omkleden welke outfit kies je (1/2)"))
        if kleding == "1":
            print("je een confortabele trainingspak gekozen")
        elif kleding == "2":
            print("je hebt en hoodie en spijkerbroek aan gedaan.")
        print("je pak je spullen en stapt uit huis")
        vervoer = input("wat voor vervoer neem jij? ((1)fiets , (2)scooter , (3)OV?  [kies een getal]")
        if vervoer == "1":
            print("je hebt de fiets gepakt en onderweg terwijl je overstak op in een dode hoek werd jij aangereden door een vrachtwagen. (slecht einde)")
            input("helaas je dood gegaan [ GAME OVER! ]")
        elif vervoer == '2':
            print("Je hebt de scooter gepakt en kwam veilig en optijd op school aan. (goed einde)")
            input("gefeliciteerd  [ GAME WON! ]")
        elif vervoer == "3":
            print("Je hebt besloten om met het OV te gaan en je kwam op het trein station aan maar je trein is vertraagd met 30 minuten komt nu te laat op school aan. (slecht einde)")
            input("helaas je hebt te laat gekomen [ GAME OVER! ]")
else:
    print("je bent thuisgebeleven omdat je geen zin had om naar school te gaan ")
    ontbijt = input("Met wat ga je mee ontbijten: Cornflakes of pannekoeken.").lower()
    if ontbijt == "cornflakes":
        print("Je hebt lekker ontbeten en gaat nu de hele dag gamen (goed einde)")
        input("Gefeliciteerd [ GAME WON! ]")
    elif ontbijt == "pannekoeken":
        print("Je ging pannekoeken bakken maar de eieren die jij had gebruikt waren bedorven") 
        print("Nu heb je het al op dus heb nu buikpijn en zit de hele dag op de WC (slecht einde)")
        print("  ")
        input("helaas je bent ziek geworden [ GAME OVER! ]")  
input("press enter to exit")


