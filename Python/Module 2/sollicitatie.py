name = input('wat is jou naam')
if name == 'robin':
    raise NameError('wat een lelijke naam')
diploma = input('heeft u een MBO 4 diploma ondernemer')
rijbewijs = input('heeft u een vrachtwagen rijbewijs')
if rijbewijs == 'nee':
    raise ValueError('leer rijden gvd')
hoed = input('bent u in bezit van een hoge hoed')
if hoed == 'nee':
    raise TypeError('beter haal je een hoed')
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
acrobatiek = int(input('hoeveel jaar doet u aan acrobatiek'))
jongleren = int(input('hoeveel jaar jongleert u'))
dieren_dressuur = int(input('hoeveel jaar dresseert u'))
ervaring = acrobatiek > 3 or jongleren > 5 or dieren_dressuur > 4

if name and diploma == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and ((geslacht == 'man' and snor == 'ja' and snor_breedte > 10) or (geslacht == 'vrouw' and haarkleur == 'ja' and haarlengte > 20)) and lengte > 150 and lengte < 220 and gewicht > 90 and gewicht < 120 and certificaat == 'ja' and ervaring:
    print('u bent geschikt voor de baan')
else:
    print('u bent niet geschikt voor de baan')