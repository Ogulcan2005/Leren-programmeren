from random import sample

naam_lijst = []
lootjes = {}
naam = True

while naam:
    toevoegen = input('wilt u een naam toevoegen ja/nee ')
    if toevoegen == 'ja':
        naam_kiezen = input('vul een naam in ')
        if naam_kiezen not in naam_lijst:
            naam_lijst.append(naam_kiezen)
        elif naam_kiezen in naam_lijst:
            print('deze naam zit er al in voeg unieke namen toe')
    elif toevoegen == "nee" and len(naam_lijst) < 3:
        print("minimaal 3 namen graag")
    else:
        naam = False

lootje_verdeling = True

while lootje_verdeling:
    schudden = sample(naam_lijst, len(naam_lijst))
    lootje_verdeling = False
    for x in range(len(naam_lijst)):
        if schudden[x] == naam_lijst[x]:   
            lootje_verdeling = True

for y in range(len(naam_lijst)):
    lootjes.update({naam_lijst[y] : schudden[y]})
print(lootjes)

