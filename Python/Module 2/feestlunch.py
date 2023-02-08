croissantjes = float(input('hoeveel kost een croissantje'))
aantal_croissantjes= int(input('hoeveel croissantjes'))
stokbroden = float(input('hoeveel kost een stokbrood'))
aantal_stokbroden = int(input('hoeveel stokbroden'))
kortingsbonnen_prijs = float(input('prijs kortingsbonnen'))
aantal_kortingsbonnen = int(input('hoeveel kortingebonnen'))

print(croissantjes * aantal_croissantjes + stokbroden * aantal_stokbroden - kortingsbonnen_prijs  * aantal_kortingsbonnen )