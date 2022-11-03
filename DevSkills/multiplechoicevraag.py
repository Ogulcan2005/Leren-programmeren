vraag = 'je gebruikt het om van variabele een zin te maken'
print(f'de vraag is: {vraag} wat is het antwoord')
print('A float')
print('B input')
print('C int')
print('D string')
antwoord = input('welk antwoord denk je')

if antwoord == 'a':
    print('het is geen float')
elif antwoord == 'b':
    print('het is geen input')
elif antwoord == 'c':
    print('fout antwoord het is geen int')
elif antwoord == 'd':
    print('correct het was string')


