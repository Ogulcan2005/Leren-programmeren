import random 
kleur = ["oranje", "blauw", "groen", "bruin"]
zak = int(input("Hoeveel m&m's wilt u in de zak"))
lijst = []

for i in range(zak):
    hoeveel = random.randint(0,3)
    print(kleur[hoeveel])
    lijst.append(kleur[hoeveel])

print(lijst)