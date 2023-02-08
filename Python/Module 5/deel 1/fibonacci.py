def get_fibo_list(fibo_lijst: list, aantal: int) -> int:
    print(fibo_lijst)
    for x in range(aantal - 2):
        fibo_lijst.append(fibo_lijst[-1] + fibo_lijst[-2]) 
        input('')
        print(fibo_lijst)
        
        
        
    
    gsnede = fibo_lijst[-1] / fibo_lijst[-2]
    return gsnede

start = [0, 1]
gulde_snede = get_fibo_list(start, 10)
print(gulde_snede)
