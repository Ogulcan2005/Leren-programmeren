from functie import aantal_bolletjes, bakje_hoorn

print("Welkom bij Papi Gelato, je mag alle smaken kiezen zolang het maar vanille ijs is.\n")
opnieuw = "ja"
while opnieuw == "ja":
    bollen = aantal_bolletjes()
    bakje_hoorn(bollen)
    opnieuw = input("Wilt u nog meer bestellen? (ja/nee): ")
    if opnieuw == "nee":
        print("Bedankt en tot ziens")
        break
    else:
        print("sorry dat snap ik niet.")
        opnieuw = "ja"
        

