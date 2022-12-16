naam_lijst = {}

while True:
    naam = input('wat is je naam? ')

    if naam == 'stop':
        break

    if naam in naam_lijst:
        if input('wilt u het bewerken ja/nee '):
            continue

    leeftijd = int(input('wat is je leeftijd? '))

    if leeftijd in naam_lijst.values():

        for n, l in naam_lijst.items():
            if l == leeftijd:
                break
        print(f'{n} is al zo oud')
        if input('toch doorgaan ja/nee ') != 'ja':
            continue
        else:
            break

    naam_lijst[naam] = leeftijd 
    #naam_lijst.update({naam : leeftijd})
print(naam_lijst)
leeftijd_list = list(naam_lijst.values())
print(leeftijd)
print(max(leeftijd))