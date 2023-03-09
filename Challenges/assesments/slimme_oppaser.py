potten_girraf = 4
potten_zebra = 4
potten_struisvogel = 2
aantal_girraf = int(input('hoeveel giraffen wilt u'))
aantal_zebra = int(input('hoeveel zebras wilt u'))
aantal_struisvogel = int(input('hoeveel struisvogels wilt u'))


def bereken_poten(girraf, zebras, struisvogel):
    aantal_potten = girraf * potten_girraf + zebras * potten_zebra + struisvogel * potten_struisvogel
    return aantal_potten
print(bereken_poten(aantal_girraf, aantal_zebra, aantal_struisvogel))
