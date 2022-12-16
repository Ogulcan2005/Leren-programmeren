# import random
# rondes = 1
# hoeveel = 10
# for x in range(20):
#     for x in range(10):
#         print(f'ronde: {rondes}')
#         rondes = rondes + 1
#         cijfer = random.randint(1, 1000)
#         print(cijfer)
#         kansen = 0
#         while kansen < 10:
#             print('raad wat het getal is in 10 kansen')
#             print(f'je hebt nog {hoeveel} kansen deze ronde')
#             raden = input()
#             raden = int(raden)
#             hoeveel -= 1
#             kansen = kansen + 1
#             som = cijfer - raden

#             if raden < cijfer:
#                 print('hoger')

#             if cijfer - raden <= 20:
#                 print("Je bent heel warm")
        
#             elif cijfer - raden <=50:
#                 print("Je bent warm")
    
#             if raden > cijfer:
#                 print('lager')
        
#             if raden == cijfer:
#                 break
    

#         if raden == cijfer:
#             kansen = str(kansen)
#             print(f'je hebt het cijfer in {kansen} kansen')
            

#         if raden != cijfer:
#             cijfer = str(cijfer)
#             print(f'sorry het cijfer was {cijfer} kansen')
import random

guesses = 6
number = random.randint(0, 1000)
win = False
print(number)

while guesses > 0:
    guess = int(input("Guess: "))

    guesses -= 1

    if guess > number:
        print("Your guess is too high", guesses, "remaining")
    elif guess < number:
        print("Your guess is too low", guesses, "remaining")
    if guess - number < 20:
        print("You are very close")
    elif guess - number < 50:
        print("You are very close")
    else:
        print("Congrats, you guessed")
        win = True
        guesses = 0

if win == False:
    print("Sorry, you didn't guess the number", number)
  