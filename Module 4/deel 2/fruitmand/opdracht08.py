from fruitmand import fruitmand

watermeloen = { 
    'name' : 'watermeloen',
    'weight' : 2500,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

volledig_gewicht = 0
for x in fruitmand:
    weight = volledig_gewicht + x['weight']
print(f'{weight}g')
    