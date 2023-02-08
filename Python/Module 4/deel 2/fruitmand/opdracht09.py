from fruitmand import fruitmand
for druif in range(fruitmand):
    if fruitmand[druif]['name'] == 'druif':
        del fruitmand[druif]
        break
for fruit in range(fruitmand):
    print(fruitmand[fruit]["color"])
