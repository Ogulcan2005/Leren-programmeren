from fruitmand import fruitmand

kleuren = {
    'yellow' : 'geel',
    'green' : 'groen',
    'orange' : 'oranje',
    'red' : 'rood',
    'brown' : 'bruin'
}
naam = []
gewicht = []
for fruit in fruitmand:
    naam.append(fruit['name'])
    naam2 = (max(naam))
    gewicht.append(fruit['weight'])
kleuren = kleuren.get('orange')
print(f'De "{max(naam)}" ({len(naam2)} letters) heeft een {kleuren} kleur en een gewicht van {gewicht[2] / 1000} kg.')


