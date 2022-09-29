gele_kaas = input('is de kaas geel')
if gele_kaas == 'ja':
    gaten = input('zitten er gaten in')
else:
    blauwe_schimmel = input('heeft de kaas blauwe schimmel')
if gaten == 'ja':
    duur = input('is de kaas belagelijk duur')
else:
    hard = input('is de kaas hard')
if duur == 'ja':
    print('de kaas die jij bedoeld is emmenthaler')
else:
    print('de kaas die jij bedoeld is leerdammer')
if hard == 'ja':
    print('de kaas die jij bedoeld is parmigiano reggiano')
else:
    print('goudse kaas')
if blauwe_schimmel == 'ja':
    korst = input('heeft de kaas een korst')
else:
    korst2 = input('heeft de kaas een korst')
if korst == 'ja':
    print('de kaas die jij bedoeld is blue de rochbaron')
else:
    print("foume d'ambert")
if korst2 == 'ja':
    print('camembert')
else:
    print('mozzarella')


    






