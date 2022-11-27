import random
kansen = 0
cijfer = random.randint(1, 1000)
print(cijfer)


while kansen < 21:
    print('raad wat het getal is in 20 kansen')
    raden = input()
    raden = int(raden)
    kansen = kansen + 1
    som = cijfer - raden

    if raden < cijfer:
        print('hoger')

    if (cijfer - raden) <= 20:
        print("Je bent heel warm")
        
    elif (cijfer - raden) <= 50:
        print("Je bent warm")
    
    if raden > cijfer:
        print('lager')
        
    if raden == cijfer:
        break
    

if raden == cijfer:
    kansen = str(kansen)
    print(f'je hebt het cijfer in {kansen} kansen')

if raden != cijfer:
    cijfer = str(cijfer)
    print(f'sorry het cijfer was {cijfer} kansen')
  