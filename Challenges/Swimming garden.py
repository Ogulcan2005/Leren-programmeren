zwembad_groote_en_diepte = 8 * 3 * 1.5
print(zwembad_groote_en_diepte)
################################################
print('-----------------------------------------------------------------------------')
# stap 2
uitgraven = 25 * zwembad_groote_en_diepte
print(f'{uitgraven}')
afvoergrond = 32.50 * 36
print(f'{afvoergrond}')
totaal = afvoergrond + uitgraven
print(f'€{totaal}')
##########################################################
print('-----------------------------------------------------------------------------')
# stap 3
km = int(input('hoeveel km'))
voorrijkosten = 250 + float(2.05 * km)
totaal2 = (f'€{uitgraven + afvoergrond + voorrijkosten}')
print(totaal2)
#######################################
print('-----------------------------------------------------------------------------')
# stap 4
hoogte = int(input('wat is jou hoogte voor je zwembad'))
breedte = int(input('wat is jou breedte voor je zwembad'))
diepte = float(input('wat is jou diepte voor je zwembad'))
hoeveel_grond = (hoogte * breedte * diepte)
print(hoeveel_grond)
###################################################
hoogte2 = int(input('wat is jou hoogte voor je zwembad'))
breedte2 = int(input('wat is jou breedte voor je zwembad'))
vierkamte = hoogte2 * breedte2
uitgraven2 = 25 * hoeveel_grond
afvoergrond2 = 32.50 * hoeveel_grond
km2 = int(input('hoeveel km'))
if voorrijkosten == km2 < 50 and hoeveel_grond < 20:
    100 + (1.25 * km2)
elif voorrijkosten == km2 > 50 and hoeveel_grond < 20:
    100 + (1.15 * km2)
elif voorrijkosten == km2 < 50 and hoeveel_grond > 20:
    250 + (2.15 * km2)
elif voorrijkosten == km2 > 50 and hoeveel_grond > 20:
    250 + (2.05 * km2)


