import random
kleurLijst = ["rood", "blauw", "groen", "geel", "bruin"]

hoeveel = int(input("Hoeveel M&M's moeten er gevoegd worden: "))
bagofmnms = {}
getal = 1

for x in range(hoeveel):
    kleur = random.choice(kleurLijst)
    if kleur not in bagofmnms:
        bagofmnms.update({kleur : getal})

    elif kleur in bagofmnms:
        bagofmnms[kleur] += 1
print(bagofmnms) 