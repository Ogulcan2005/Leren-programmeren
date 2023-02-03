def multiplier(cijfer: int):

    for x in range(1, 11):
        print(f'{x}x{cijfer} = {x * cijfer}')
cijfer = int(input('hoeveel wilt u'))
multiplier(cijfer)