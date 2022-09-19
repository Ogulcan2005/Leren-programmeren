toegangsticket = float(input('ticketprijs'))
VIP_VR_GameSeat_per_5_minuten = float(input('vr_prijs_per_5_minuut'))
aantal_personen = int(input('hoeveel personen'))
hoeveel_keer_vr_per_5_min = int(input('hoeveel keer vr'))

print(toegangsticket * aantal_personen + VIP_VR_GameSeat_per_5_minuten * hoeveel_keer_vr_per_5_min * aantal_personen)

croissantjes = float(input('hoeveel kost een croissantje'))
aantal_croissantjes= int(input('hoeveel croissantjes'))
stokbroden = float(input('hoeveel kost een stokbrood'))
aantal_stokbroden = int(input('hoeveel stokbroden'))
kortingsbonnen_prijs = float(input('prijs kortingsbonnen'))
aantal_kortingsbonnen = int(input('hoeveel kortingebonnen'))

print(croissantjes * aantal_croissantjes + stokbroden * aantal_stokbroden - kortingsbonnen_prijs  * aantal_kortingsbonnen )