prijs_iphone_13 = int(input('prijs van iphone'))
prijs_samsung_s22 = int(input('prijs van samsung'))
prijs_asus_zenfone_9 = int(input('prijs van asus'))
prijs_verschil = (prijs_samsung_s22 - prijs_asus_zenfone_9)
telefoon = str('iphone')
telefoon_2 = str('samsung')
telefoon3 = str('asus zenfone 9')
prijs_verschil2 = prijs_iphone_13 - prijs_asus_zenfone_9

print(f'de {telefoon} is het duurst, de telefoon kost: €{prijs_iphone_13} ')
print(f'de {telefoon3} is het goedkoopst, de telefoon kost: €{prijs_asus_zenfone_9}')
print(f'de {telefoon_2} zit er tussenin met: €{prijs_samsung_s22}')
print(f'het advies is dus de {telefoon3} te kopen deze is namelijk €{prijs_verschil} goedkoper dan de {telefoon_2} en €{prijs_verschil2} goedkoper dan de {telefoon} ')