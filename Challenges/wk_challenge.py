import random 
land1 = input('welk land voor groep a')
land2 = input('welk land voor groep a')
land3 = input('welk land voor groep a')

goals = int(input('hoeveel goals'))
goals2 = int(input('hoeveel goals'))

wedstrijd1 = (f'{land1} tegen {land2}')
doelsaldo = goals - goals2
doelsaldo2 = goals2 - goals
punten = 0

print(F'Wedstrijd {wedstrijd1} eindigde in: {goals} - {goals2}')
if goals > goals2:
    print(f'Winnaar is {land1}')
    punten += 3
    print(f'punten {punten}; doelsaldo is: {doelsaldo}')

if goals < goals2:
    print(f'winnaar is {land2}')
    print(f'doelsaldo is: {doelsaldo2}')
    punten += 3
    print(f'punten {punten}; doelsaldo is: {doelsaldo2}')












# wedstrijd2 = (f'{land2} tegen {land3}')
# wedstrijd3 = (f'{land1} tegen {land3}')
# print(F'{wedstrijd2} eindigde in: {goals} - {goals2}')
# print(F'{wedstrijd3} eindigde in: {goals} - {goals2}')