import random

num1 = random.randint(1, 10)
num2 = random.randint(5, 15)


number = input(f'En weet jij wat {num1} + {num2} is?')
number = num1 + num2
if (number == num1 + num2):
    print('Dat is juist')
