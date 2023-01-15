def hello(cijfer: int) -> str:
    cijfer = int(input('hoeveel wilt u'))
    nummer = 1
    for x in range(cijfer):
        print(f'Hello from function town {nummer}!')
        nummer += 1
hello(1)


