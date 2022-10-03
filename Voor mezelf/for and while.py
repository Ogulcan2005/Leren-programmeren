from re import X


zin = 'hallo wereld'
x = 0
for c in (0, 1, 2):
    print(zin)
    for d in (0, 1, 2):
        for e in (0, 1, 2):
            x = x + 1
        print(zin, c, d, e, 'x =', x)