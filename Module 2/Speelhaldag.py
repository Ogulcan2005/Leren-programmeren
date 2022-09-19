toegangsticket = float(input('ticketprijs'))
VIP_VR_GameSeat_per_5_minuten = float(input('vr_prijs_per_5_minuut'))
aantal_personen = int(input('hoeveel personen'))
hoeveel_keer_vr_per_5_min = int(input('hoeveel keer vr'))

print(toegangsticket * 4 + VIP_VR_GameSeat_per_5_minuten * 9 * 4)

print(toegangsticket * aantal_personen + VIP_VR_GameSeat_per_5_minuten * hoeveel_keer_vr_per_5_min * aantal_personen)


