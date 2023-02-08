geel = input('is de kaas geel?')

if geel == "ja":
    gaten = input('zitten er gaten in?')
    if gaten == "ja":
        duur = input('is de kaas belagelijk duur?')
        if duur == "ja":
            print('de kaas die u bedoeld is emmenthaler')
        else:
            print('de kaas die u bedoeld is leerdammer ')
    else:
        hard = input('is de kaas hard als steen')
        if hard == 'ja':
            print('de kaas die u bedoel is parmigiano reggiano')
        else:
            print('de kaas die u bedoeld is goudse kaas')
else:
    blauw = input('heeft de kaas blauwe schimmel')
    if blauw == 'ja':
        korst1 = input('heeft de kaas een korst')
        if korst1 == 'ja':
            print('de kaas die u bedoeld is blue de rochbaron')
        else:
            print('de kaas die u bedoeld is foume dambert')
    else:
        korst2 = input('heeft de kaas een korst')
        if korst2 == 'ja':
            geur = input('heeft de kaas een geur')
            if geur == 'ja':
                print('de kaas die u bedoeld is camembert')
            else:
                print('de kaas die u bedoeld is brie')
        else:
            print('de kaas die u bedoeld is mozzarella')