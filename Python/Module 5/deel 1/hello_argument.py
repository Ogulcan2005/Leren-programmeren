def hello(cijfer: int) -> str:
    zin = ''
    for x in range(1, cijfer + 1):
        zin += f'Hello from function town {x}!\n'
    return zin
print(hello(10))


