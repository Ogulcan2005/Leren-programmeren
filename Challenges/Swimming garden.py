# stap 1
zwembad_groote_en_diepte = 8 * 3 * 1.5
print(zwembad_groote_en_diepte)
################################################
# stap 2
uitgraven = 25 * zwembad_groote_en_diepte
print(f'{uitgraven}')
afvoergrond = 32.50 * 36
print(f'{afvoergrond}')
totaal = afvoergrond + uitgraven
print(f'€{totaal}')
##########################################################
# stap 3
voorrijkosten = 250 + float(2.05 * 60)
totaal2 = (f'€{uitgraven + afvoergrond + voorrijkosten}')
print(totaal2)
#######################################
# stap 4
hoogte = int(input('wat is jou hoogte voor je zwembad'))
breedte = int(input('wat is jou breedte voor je zwembad'))
diepte = float(input('wat is jou diepte voor je zwembad'))
hoeveel_grond = hoogte * breedte * diepte
print(hoeveel_grond)
###################################################
#stap 5


