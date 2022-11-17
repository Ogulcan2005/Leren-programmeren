getal = 50
som = 50
zin = '50'

while som < 1000:
    getal += 1
    som = som + getal
    zin += (f' + {getal}')
    print(f'{zin} = {som}')
