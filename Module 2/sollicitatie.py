diploma = input('heeft u een MBO 4 diploma ondernemer')
rijbewijs= input('heeft u een vrachtwagen rijbewijs')
hoed = input('bent u in bezit van een hoge hoed')
geslacht = input('wat is uw geslacht man of vrouw')
if geslacht == 'man':
    snor = input('heeft u een snor')
    if snor == 'ja':
        snor_breedte = int(input('wat is uw snor breedte in cm'))          
else:
    haarkleur = (input('heeft u rood haar'))
    haarlengte = int(input('hoelang is uw haar in cm'))        
lengte = int(input('hoelang bent u'))
gewicht = int(input('wat is uw lichaamsgewicht'))
certificaat = input('heeft u een overleven met gevaarlijk personeel certificaat')
ervaring = input('praktijkervaring met dieren-dressuur of ervaring met jongleren of praktijkervaring met acrobatiek')
if ervaring == 'acrobatiek':
    acrobatiek = int(input('hoe jaar ervaring hebt u met acrobatiek'))
    acrobatiek > 3
elif ervaring == 'jongleren':
    jongleren = int(input('hoeveel jaar ervaring hebt u met jongleren'))
    jongleren > 5
    if ervaring == 'dieren-dressuur':
        dieren_dressuur = int(input('hoeveel jaar ervaring hebt u met dieren-dressuur'))
        dieren_dressuur > 4

if (diploma == 'ja') and (rijbewijs == 'ja') and (hoed == 'ja') and (geslacht == 'man' and snor == 'ja' and snor_breedte > 10) or (geslacht == 'vrouw' and haarkleur == 'ja' and haarlengte > 20) and (lengte > 150 and lengte < 220) and (gewicht > 90 and gewicht < 120) and (certificaat == 'ja') and (ervaring and acrobatiek > 3 and jongleren > 5 and dieren_dressuur > 4):
    print('geschikt voor de baan')
else:
    print("je bent niet geschikt")