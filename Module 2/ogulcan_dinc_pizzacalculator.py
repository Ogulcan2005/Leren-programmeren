small_pizza = 9.99
aantal_small_pizzas = int(input('hoeveel small pizzas wilt u'))
medium_pizza = 15.49
aantal_medium_pizzas = int(input('hoeveel medium pizzas wilt u'))
large_pizza = 17.99
aantal_large_pizzas = int(input('hoeveel large pizzas wilt u'))
Name = input('wat jou naam')
Adres = input('wat is je adres')
huisnummer = input('wat is jou huisnummer')
Postcode = input('wat is je postcode')
Woonplaats = input('wat is je woonplaats')
totaal = aantal_small_pizzas * small_pizza + aantal_medium_pizzas * medium_pizza + aantal_large_pizzas * large_pizza

print('----------------------------------------------------------')
print('|     Name :' + Name)
print('|     Adres :' + Adres)
print('|     Huisnummer :' + huisnummer)
print('|     Postcode  :' + Postcode)
print('|     Woonplaats :' + Woonplaats)
print('|                                          ')
print(f"|aantal small pizzas {aantal_small_pizzas} prijs €{small_pizza} totaal €{aantal_small_pizzas * small_pizza}")
print(f"|aantal medium pizzas {aantal_medium_pizzas} prijs €{medium_pizza} totaal €{aantal_medium_pizzas * medium_pizza}")
print(f"|aantal large pizzas {aantal_large_pizzas} prijs €{large_pizza} totaal €{aantal_large_pizzas * large_pizza}")
print(f"|totatle prijs                             €{totaal}")
print('--------------------------------------------------------')