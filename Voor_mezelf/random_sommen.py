import random
def addition(number1: int, number2: int) -> int:
    antwoord = number1 + number2
    return antwoord

def subtraction(nummer1: int, nummer2: int) -> int:
    antwoord2 = nummer1 - nummer2
    return antwoord2

def multiplication(nb1: int, nb2: int) -> int:
    antwoord3 = nb1 * nb2
    return antwoord3

def division(nb3: int, nb4: int) -> int:
    antwoord4 = nb3 / nb4
    return antwoord4

lijst = [addition, multiplication, subtraction, division]

aantal = int(input('hoeveel sommen wil je'))
for x in range(aantal):
    sommen = random.choice(lijst)
    getal1 = random.randint(1,10)
    getal2 = random.randint(1,10)
    if sommen == addition:
        print(f'{getal1} + {getal2}')
    elif sommen == multiplication:
        print(f'{getal1} * {getal2}')
    elif sommen == subtraction:
        print(f'{getal1} - {getal2}')
    elif sommen == division:
        print(f'{getal1} / {getal2}')
    vraag = sommen(getal1, getal2)
    antwoord = int(input('wat is het antwoord'))
    if vraag == antwoord:
        print('goed bezig')
    else:
        print('sorry dat is fout')
    
