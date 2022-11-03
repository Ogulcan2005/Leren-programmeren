from random import Random, randint

aantal_complimenten = int(input('hoeveel complimenten wil je'))
naam = input('wat is jou naam')
vorige_random_getal = 0

for x in range (aantal_complimenten):
    random_getal = randint(1,4)
    while random_getal == vorige_random_getal:
        random_getal = randint(1,4)
    print(f'random_getal = {random_getal}, vorige = {vorige_random_getal}')
    
    vorige_random_getal = random_getal

    print(f'random_getal = {random_getal}, vorige = {vorige_random_getal}')

    if random_getal == 1:
        print(f'je bent geweldig {naam}')
    elif random_getal == 2:
        print(f'je bent een topgozer {naam}')
    elif random_getal == 3:
        print(f'je bent de beste {naam}')
    elif random_getal == 4:
        print(f'super bezig {naam}')