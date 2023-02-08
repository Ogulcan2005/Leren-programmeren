print('Je hebt een broer die een schat zoeker was maar stierf tijdens het zoeken van de grootste schat terwereld')
print('een schat uit de 16e eeuw jaren later probeer jij de schat te zoeken als aandenking aan hem')
print('je probeerd eerst de kaart te stelen die naar de schat leidt maar faalt later ontmoet je iemand die je broer kende en hielp schatten te zoeken')
print('nu bied hij jou hulp aan om de kaart te stelen en de schat te vinden.')
print("")
hulp_bieden = input('accepteer jij zijn hulp ja/nee?')
if hulp_bieden == 'ja':
    print('je accepteert johns hulp en hij')
    informatie = input('wil je informatie krijgen over de kaart ja/nee?')
    if informatie == 'ja':
        print("")
        print('je krijgt info over de schat die je niet eerder wist.')
        print('om de schat te vinden via de kaart hebben ze eerst 2 gouden kruizen nodig.')
        print("")
        plan = input('de vriend van je broer John heeft een plan om de kruizen te vinden wil je het plan horen ja/nee?')
        if plan == 'ja':
            print("")
            print('1 van de 2 kruizen wordt geveild in een museum') 
            print('wij gaan daar heen en ik doen alsof ik mee doe aan de veiling terwijl jij de kruis steelt zonder dat iemand het merkt.')
            print('jullie zijn bij de veiling en gaan het plan volgen.')
            print('terwijl je het plan volgt ontmoet john een oude vriend die ook naar de schat zoekt maar hem vroeger heeft veraden')
            print("")
            gelukt = input('is het plan gelukt ja/nee?')
            if gelukt == 'ja':
                print("")
                print('jullie hebben de kruis en gaan nu weg en gaab opzoek naar de 2e kruis maar john zegt dat dat niet hoeft')
                print('hij heeft een vriendin jessica die de 2e kruis en de kaart heeft samen gaan we de schat zoeken')
                print('en ze hebben jou hulp nodig om met de 2 kruizen de schat te vinden')
                print("")
                kaart = input('vindt je de aanwijzing op de kaart ja/nee?')
                if kaart == 'ja':
                    print('je vindt de aanwijzing naar de schat en gaat er heen met john en jessica ')
                    print('de schat ligt ergens in een onbekend eilinfd in het westen van nederland')
                    print("")
                    GaanofNiet = input('gaan jullie nu meteen naar de locatie of niet ja/nee?')
                    if GaanofNiet == 'ja':
                        print("")
                        print('jullie hebben een bood geregeld en gaan naar de schat')
                        print('maar johns oude vriendin volgt hun zonder dat ze het merken')
                        print('jullie zijn op het eiland en zoeken nu naar aanwijzingen')
                        print('john ziet een waterval waar een fel licht van komt hij ging het onderzoeken en vondt een geheime doorgang')
                        print('hij riep jou en jessica om te vertellen dat hij het heedt gevonden')
                        print("")
                        schat = input('nemen jullie al het goud mee of zoveel als je kunt dragen alles/deel?')
                        if schat == 'deel':
                            print("")
                            print('jullie nemen ieder zoveel moggelijk goud als je kunt dragen')
                            print('en johns vriedin neemt ook zoveel moggelijk goud mee')
                            print('iedereen eindigt met het goud en een mooi leven')
                            print('Het Einde')
                            exit()
                        else:
                            print('jullie gaan voor deel want jullie kunnen nooit al dat goud dragen')
                            print('zelfde gaat voor johns vriedin die ook wat goud heeft kunnen pakken')
                            exit()
                    else:
                        print('jullie gaan morgen in de ochtend maar terwijl jullie slapen brak')
                        print('johns vriedin in jullie kamer en stal de kaart en de cordinaten van de schat')
                        exit()
                else:
                    print('je kunt de aanwijzing niet vinden en geeft het op pech gehad')
                    exit()
            else:
                print('het plan is niet gelukt en johns vriendin heeft de kruis')
                exit()
        else:
            print('je wilt het plan niet horen dat wordt lastig maar je maakt je eigen plan')
            print('je maakt een plan B en dat is door te improviseren en het')
    else:
        print('zonder informatie kun je geen plan bedenken idioot')
        exit()
else:
    print('je zult de schat nooit vinden zonder john')
    exit()
