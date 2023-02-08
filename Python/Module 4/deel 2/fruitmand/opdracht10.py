from fruitmand import fruitmand
from operator import itemgetter
fruitmand = sorted(fruitmand , key = itemgetter('weight'),reverse=True)
for weight in fruitmand:
        print(weight['name'], weight['weight'])