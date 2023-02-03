import random
def random_sommen(aantal: int):
    for x in range(aantal):
        n1 = random.choice(1, 500)
        n2 = random.choice(1, 500)
        som = n1 + n2
        

print(random_sommen(7))