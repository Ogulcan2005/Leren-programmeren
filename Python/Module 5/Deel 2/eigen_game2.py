from data_lijst import data_lijst
print('Je hebt een broer die een schat zoeker was maar stierf tijdens het zoeken van de grootste schat terwereld')
print('een schat uit de 16e eeuw jaren later probeer jij de schat te zoeken als aandenking aan hem')
print('je probeerd eerst de kaart te stelen die naar de schat leidt maar faalt later ontmoet je iemand die je broer kende en hielp schatten te zoeken')
print('nu bied hij jou hulp aan om de kaart te stelen en de schat te vinden.\n')



def handle_scenario(scenario : dict, inventory: list) -> bool:
    print(scenario['vraag'])
    antwoord_op_vraag = input('wat is je antwoord ')

    heeft_item = True
    if len(scenario['needed_item']) > 0 and scenario['needed_item'][0] not in inventory:
        heeft_item = False

    print(heeft_item)
    # check hier of je een needed item hebt en of dat in je inventry zit
    if antwoord_op_vraag in scenario['antwoord'] and heeft_item:
        print(scenario['tekst_waar'])
        
        if len(scenario['to_pick']) > 0:
            if input(f"Pak je het {scenario['to_pick'][0]} op?") == "ja":
                inventory.append(scenario['to_pick'][0])    

        return True, items
    else:
        print(scenario['tekst_niet_waar'])
        print('GAME OVER\n')
        return False, items

teller = 0
door_spelen = ''
items = []

while True:
    door, items = handle_scenario(data_lijst[teller], items)
    print(items)
    if not door:
        break
    teller += 1
    if teller > 6:
        break

    