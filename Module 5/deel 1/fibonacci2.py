def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("hoevaak wilt u het"))

for i in range(n):
    print(fibonacci(i))

# def fibonacci2(fibo_list: list, max: int) -> int:
#     return fibo_list

# lijst = [0,1]
# fibo = lijst[-2] + lijst[-1]
# while lijst[-2] < 1000:
#     fibo = lijst[-2] + lijst[-1]
#     lijst.append(fibo)

# print(fibonacci2(lijst, 1000))




