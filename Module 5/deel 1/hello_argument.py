def hello(cijfer: int) -> str:
    number = int(input('hoevaak wilt u'))
    nummer = 1
    for x in range(number - 1):
        print(f'Hello from function town {nummer}!')
        nummer += 1
    return f'Hello from function town {nummer}!'
print(hello(0))


