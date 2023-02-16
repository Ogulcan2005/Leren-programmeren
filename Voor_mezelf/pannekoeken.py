from re import MULTILINE


aantal_pannenkoeken = int(input('hoeveel pannenkoeken?'))
bloem = 500
eieren = 3
melk = 800
zout = 1
boter = 50

multiline_zin = f"""Voor {aantal_pannenkoeken} heb je nodig:
{bloem/20*aantal_pannenkoeken} gram bloem
{eieren/20*aantal_pannenkoeken} eieren
{melk/20*aantal_pannenkoeken} melk ml
{zout/20*aantal_pannenkoeken} zout
{boter/20*aantal_pannenkoeken} boter gram"""
print(multiline_zin)