def fibonacci(count) -> int:
    getal1 = int(input('waar wil je mee beginnen'))
    getal2 = int(input('wat is het tweede getal'))

    print(getal1)
    print(getal2)


    counter = 1
    while counter <= count - 2:
        getal3 = getal1 + getal2
        getal1 = getal2
        getal2 = getal3
        print(getal3)

        counter += 1

hoe_vaak_om_rekenen = int(input('hoe vaak wilt u dat hij blijft rekenen'))
fibonacci(hoe_vaak_om_rekenen)