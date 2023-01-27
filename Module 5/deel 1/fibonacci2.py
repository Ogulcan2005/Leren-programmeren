def fibonacci(lijst: list, max: int) -> list:
    if len(lijst) >= max:
        print(lijst)
        gulde = lijst[-1] / lijst[-2]
        return gulde
    else:
        lijst.append(lijst[-2] + lijst[-1])
        return fibonacci(lijst, max)
    


hoevaak = int(input('hoevaak wil u dat hij elkaar optelt'))
print(fibonacci([0, 1], hoevaak))


# def fibonacci2(fibo_list: list, max: int) -> int:
#     return fibo_list

# lijst = [0,1]
# fibo = lijst[-2] + lijst[-1]
# while lijst[-2] < 1000:
#     fibo = lijst[-2] + lijst[-1]
#     lijst.append(fibo)

# print(fibonacci2(lijst, 1000))




