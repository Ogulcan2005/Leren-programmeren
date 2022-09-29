fysiek = input('is het spel fysiek')
if fysiek == 'ja':
    bordspel = input('is het een bordspel')
    if bordspel == 'nee':
        oranje = input('is het spel oranje')
        if oranje == 'ja':
            print('het is het kaart spel')
        elif oranje == 'nee':
            print('het is sushi go')
    elif bordspel == 'ja':
        treintjes = input('heeft het spel treintjes')
        if treintjes == 'nee':
            print('catan')
elif fysiek == 'ja':
    sport = input('is het een sportspel')
    if sport == 'ja':
        print('fifa 23')
    elif sport == 'nee':
        print('aoe 4')