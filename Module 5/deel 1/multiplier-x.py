def multiplier(cijfer: int):
    cijfer = int(input('hoeveel wilt u'))
    for x in range(1, 11):
        print(f'{x}x{cijfer} = {x * cijfer}')
multiplier(10)