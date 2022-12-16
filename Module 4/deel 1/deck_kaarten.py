from random import randint, random,shuffle
kleur = ['harten', 'klaveren', 'schoppen', 'ruiten']
kaarten = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'boer', 'vrouw', 'heer', 'aas']
deck = []
for x in range(4):
    for y in range(13):
        deck.append(kleur[x] + ' ' + str(kaarten[y]))
for z in range(2):
    deck.append('joker')
shuffle(deck)
print(deck)
for a in range(1, 8):
    print(f'kaart {a}: {deck[0]}')
    deck.pop(0)
print(deck)
