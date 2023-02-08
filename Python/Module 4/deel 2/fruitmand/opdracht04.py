from fruitmand import fruitmand 
from random import randint
hoeveel = int(input('hoeveel fruit wilt u' ))
for x in range(hoeveel):
    fruit = (fruitmand[randint(0,6)]['name'])
    print(fruit)

