def calc_prijs(lijstje) -> float:
    PRIJS_OLLIEBOL = 1.05
    PRIJS_10_OLLIEBOL = 7.50
    PRIJS_BEIGNET = 1.50
    prijs_bol = 0
    prijs_bol = (lijstje["oliebol"] // 10) * PRIJS_10_OLLIEBOL
    prijs_bol += (lijstje["oliebol"] % 10) * PRIJS_OLLIEBOL
    prijs_bol = lijstje["oliebol"] * PRIJS_OLLIEBOL
    prijs_beig = lijstje["appelbeignet"] * PRIJS_BEIGNET
    prijs_totaal = prijs_bol + prijs_beig
    return round(prijs_totaal,2)

lijstje_dict = {"oliebol": 0, "appelbeignet": 0}

lijstje_dict["oliebol"] = int(input("Hoeveel oliebollen wilt u? "))
lijstje_dict["appelbeignet"] = int(input("Hoeveel appelbeignets wilt u? "))

totaal_prijs = calc_prijs(lijstje_dict)

print(totaal_prijs)

