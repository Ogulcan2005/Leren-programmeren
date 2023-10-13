from functie import *

print("Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n")
opnieuw = "ja"
while opnieuw == "ja":
    aantal_bolletjes()
    bakje_hoorn(aantal_bolletjes)
    if opnieuw == "nee":
        print("Bedankt en tot ziens")
        break
    else:
        print('Sorry, dat snapik niet...')
        opnieuw = input("Wilt u nog meer bestellen ")

