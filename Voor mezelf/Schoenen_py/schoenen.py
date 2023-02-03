from schoenen_data import schoenen_lijst
# opdracht 1
# print(schoenen_lijst[0])
# print(schoenen_lijst[1])
# print(schoenen_lijst[2])

#opdracht 2
# vraag_merk = input('welke merk wilt u')
# for x in schoenen_lijst:
#     if vraag_merk in x['merk']:
#         print(x['model'])
#         print(x['prijs'])

#opdracht3
# vraag_merk = input('welke merk wilt u')
# for x in schoenen_lijst:
#     if vraag_merk in x['merk']:
#         print(x['merk'])
#         if x['kleur'] == 'wit':
#             print(x['kleur'])
#             if x['prijs'] > 100:
#                 print(x['prijs'])

#opdracht 4
vraag_maat = int(input('welke maat wilt u'))
for x in schoenen_lijst:
    if vraag_maat in x['maten']:
        print(x['merk'])
        if x['kleur'] == 'wit':
            print(x['kleur'])
            if x['prijs'] > 100:
            print(x['prijs'])



