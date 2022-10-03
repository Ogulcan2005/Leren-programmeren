small_pizza = 9.99
while True:
    try:
        aantal_small_pizzas = int(input('hoeveel small pizzas wilt u'))
        break
    except ValueError:
        print('gebruik getallen')
medium_pizza = 15.49
while True:
    try:
        aantal_medium_pizzas = int(input('hoeveel medium pizzas wilt u'))
        break
    except ValueError:
        print('gebruik getallen')
large_pizza = 17.99
while True:
    try:
        aantal_large_pizzas = int(input('hoeveel large pizzas wilt u'))
        break
    except ValueError:
        print('gebruik getallen')

name = input('wat jou naam')
adres = input('wat is je adres')
huisnummer = input('wat is jou huisnummer')
postcode = input('wat is je postcode')
woonplaats = input('wat is je woonplaats')
totaal = aantal_small_pizzas * small_pizza + aantal_medium_pizzas * medium_pizza + aantal_large_pizzas * large_pizza

print('----------------------------------------------------------')
print('|     name :' + name)
print('|     adres :' + adres)
print('|     huisnummer :' + huisnummer)
print('|     postcode  :' + postcode)
print('|     woonplaats :' + woonplaats)
print('|                                          ')
print(f"|aantal small pizzas {aantal_small_pizzas} prijs €{small_pizza} totaal €{aantal_small_pizzas * small_pizza}")
print(f"|aantal medium pizzas {aantal_medium_pizzas} prijs €{medium_pizza} totaal €{aantal_medium_pizzas * medium_pizza}")
print(f"|aantal large pizzas {aantal_large_pizzas} prijs €{large_pizza} totaal €{aantal_large_pizzas * large_pizza}")
print(f"|totatle prijs                             €{totaal}")
print('--------------------------------------------------------')