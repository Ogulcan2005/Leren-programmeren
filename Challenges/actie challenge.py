getal1 = int(input('voer getal 1'))
getal2 = int(input('voer getal 2'))
actie = input('welke actie wenst u')


if actie == 'a':
    antwoord = getal1 - getal2
elif actie == 'o':
    zin = 'optellen'
    antwoord = getal1 + getal2
elif actie == 'k':
    if getal1 > getal2:
        zin = 'volgorde (k)' + str(getal2) + ', ' + str(getal1)
    else:
        zin = 'volgorde (k)' + str(getal1) + ', ' + str(getal2)

print(zin)
if actie == 'k' and actie == 'g':
    print(antwoord)