antwoord = input('ja of nee')
while antwoord not in ('ja', 'nee'):
    antwoord = input('ja of nee')
    print('gestopt')

while True:
    antwoord = input('ja of nee')
    if antwoord in ('ja', 'nee'):
        break