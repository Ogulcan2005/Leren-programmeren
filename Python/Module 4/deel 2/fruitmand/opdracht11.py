from fruitmand import fruitmand
kleuren = []
for fruit in fruitmand:
    if fruit['color'] not in kleuren:
        kleuren.append(fruit['color'])
# kleur
a = True
while a == True:
        kleur = input ('kies een kleur (yellow, green, red, orange, brown)')
        if kleur in kleuren:
            print(f'je hebt {kleur} gekozen')
            a = False
        else:
            print('kies een kleur die in de lijst staat')
# aantal ronde en niet ronde
rond = 0
niet_rond= 0
for fruit in fruitmand:
    kleuren = fruit['color']
    if kleuren == kleur:
        fruit['round']
        if fruit['round'] == True:
            rond += 1 
        elif fruit['round'] == False:
            niet_rond += 1
print(f'het aantal ronde fruit is: {rond}')
print(f'het aantal niet ronde fruit is: {niet_rond}')     

x1 = rond - niet_rond
x2 = niet_rond - rond       
# uitslag
if rond > niet_rond:
    print(f'Er zijn {x1} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif rond < niet_rond:
    print(f'Er zijn {x2} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}')
elif rond == niet_rond:
    print(f'Er zijn {rond} ronde vruchten en {niet_rond} niet ronde vruchten in de kleur {kleur}')