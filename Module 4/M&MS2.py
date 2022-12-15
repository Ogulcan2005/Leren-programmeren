from random import randint
kleur = ['rood', 'blauw', 'groen', 'geel', 'bruin']
aantal = int(input("Hoeveel m&m's wilt u in de zak"))
zak = []

for x in range(aantal):
    zak.append(kleur[randint(0,4)])

bagofmnms = {
    'rood' : zak.count('rood'),
    'groen' : zak.count('groen'),
    'geel' : zak.count('geel'),
    'blauw' : zak.count('blauw'),
    'bruin' : zak.count('bruin'),
}
print(bagofmnms)
