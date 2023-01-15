def multiplier(cijfer: int) -> str:
    cijfer = int(input('hoeveel wilt u'))
    nummer = 1
    for x in range(10):
        print(f'{nummer}x{cijfer} = {nummer * cijfer}')
        nummer += 1
multiplier(int)