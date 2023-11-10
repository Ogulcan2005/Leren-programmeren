def aantal_bolletjes() -> int:
    return int(input("Hoeveel bolletjes wilt u? "))

def bakje_hoorn(bollen) -> str:
    if bollen < 4:
        bakjeofhoorn = input(f"Wilt u deze {bollen} bolletje(s) in een hoorntje of een bakje? ")
        while bakjeofhoorn not in ["bakje", "hoorn"]:
            print("Sorry, dat snap ik niet...")
            bakjeofhoorn = input(f"Wilt u deze {bollen} bolletje(s) in een hoorntje of een bakje? ")
        print(f"Hier is uw {bakjeofhoorn} met {bollen} bolletje(s).")
        return bakjeofhoorn
    elif bollen < 9:
        print(f"Dan krijgt u van mij een bakje met {bollen} bolletjes.")
        print(f"Hier is uw bakje met {bollen} bolletje(s).")
        return "bakje"
    else:
        print("Sorry, zulke grote bakken hebben we niet.")

def bestelling():
    Bolletjes = 1.10
    Horrentjes = 1.25
    Bakjes = 0.75
    opnieuw = "ja"

    totaal_bollen = 0
    totaal_bakje = 0
    totaal_hoorn = 0

    while opnieuw == "ja":
        aantal_bollen = aantal_bolletjes()
        bakjeofhoorn = bakje_hoorn(aantal_bollen)
        totaal_bollen += aantal_bollen
        if bakjeofhoorn == "bakje":
            totaal_bakje += 1
        elif bakjeofhoorn == "hoorn":
            totaal_hoorn += 1
        opnieuw = input("Wilt u nog meer bestellen? (ja/nee) ")

    if opnieuw == "nee":
        print("Uw bestelling:")
        print("----[Papi Gelato]----")
        print(f"bolletjes {totaal_bollen} x {Bolletjes}: {totaal_bollen * Bolletjes:.2f}")
        print(f"bakjes {totaal_bakje} x {Bakjes}:  {totaal_bakje * Bakjes}")
        print(f"hoorntjes {totaal_hoorn} x {Horrentjes}:  {totaal_hoorn * Horrentjes}")
        totale_prijs = (totaal_bollen * Bolletjes) + (totaal_bakje * Bakjes) + (totaal_hoorn * Horrentjes)
        print(f"Totale prijs: €{totale_prijs:.2f}")
        print("Bedankt en tot ziens")


