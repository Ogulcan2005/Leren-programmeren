boodschappen_lijst = {}
items_list= []
aantal_list= []

#items en aantal
while True:
    items = input('Voeg uw item toe:  ')
    if items in items_list:
        print ('De item staat in je boodschappenlijstje. Voer een nieuw totaal in.')
    items_list.append(items)
    aantal = int(input(f'Hoeveel {items} wil je? '))
    aantal_list.append(aantal)
    extra = input("Wil je meer items toevoegen? (ja/nee): \n")
    if extra != "ja":
      break

for x in items_list:
    for value in aantal_list:
        boodschappen_lijst[x] = value
        aantal_list.remove(value)
        break

if extra == 'nee':
    print ('[------BOODSCHAPENLIJST------]')
for key, value in boodschappen_lijst.items(): 
    print(f"{value}x   {key}") 
print('----------------------------')