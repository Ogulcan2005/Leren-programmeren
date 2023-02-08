def vraag_persoon() -> dict:
    dictionary = {}
    naam = input('wat is je naam')
    leeftijd = input('wat is je leeftijd')
    dictionary.update({'naam': naam })
    dictionary.update({'leeftijd' : leeftijd})
    return dictionary

lijst = []
while input('Toets enter om door te gaan of stop om te printen:') == '' :
    lijst.append(vraag_persoon())
else:
    for x in lijst:
        print(f"{x['naam']} is {x['leeftijd']}")