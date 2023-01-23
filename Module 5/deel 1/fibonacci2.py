def fibonacci(lijst: list, max: int) -> list:
    if lijst[-2] >= max:
        return lijst
    else:
        lijst.append(lijst[-2] + lijst[-1])    
        return fibonacci(lijst, max)

print(fibonacci([0, 1], 100))


# def fibonacci2(fibo_list: list, max: int) -> int:
#     return fibo_list

# lijst = [0,1]
# fibo = lijst[-2] + lijst[-1]
# while lijst[-2] < 1000:
#     fibo = lijst[-2] + lijst[-1]
#     lijst.append(fibo)

# print(fibonacci2(lijst, 1000))




