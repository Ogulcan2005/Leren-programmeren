grootste = 0
kleinste = 1000
aantal_deelbaar_3 = 0
for x in range(10):
    getal = int(input('welke 10 getallen wilt u (tussen de 0 en 1000):'))
    if getal > grootste:
        grootste = getal
    elif getal < kleinste:
        kleinste = getal
    if getal % 3 == 0:
        aantal_deelbaar_3 = aantal_deelbaar_3 + 1


print(f'het grootste getal is: {grootste}')
print(f'het kleinste getal is: {kleinste}')
print(f'aantal deelbaar door 3 is: {aantal_deelbaar_3}')