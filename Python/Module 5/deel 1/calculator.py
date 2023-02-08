def addition(number1: float, number2: float) -> float:
    antwoord = number1 + number2
    return antwoord

def subtraction(nummer1: float, nummer2: float) -> float:
    antwoord2 = nummer1 - nummer2
    return antwoord2

def multiplication(nb1: float, nb2: float) -> float:
    antwoord3 = nb1 * nb2
    return antwoord3

def division(nb3: float, nb4: float) -> float:
    antwoord4 = nb3 / nb4
    return antwoord4

n1 = float(input('welk getal wil je mee beginen'))

while n1 > True:
    choice = input('wat wilt u doen? A) getallen optellen, B) getallen aftrekken, C) getallen vermenigvuldigen, D) getallen delen, E) getal ophogen, F) getal verlagen, G) getal verdubbelen of H) getal halveren?')
    
    if choice == 'a':
        n2 = float(input('met welk getal wilt u het vermenigvuldigen'))
        print(addition(n1, n2))
        n1 = addition(n1, n2)
    elif choice == 'b':
        n2 = float(input('welk tweede getal wil je'))
        print(subtraction(n1, n2))
        n1 = subtraction(n1, n2)
    elif choice == 'c':
        n2 = float(input('welk tweede getal wil je'))
        print(multiplication(n1, n2))
        n1 = multiplication(n1, n2)
    elif choice == 'd':
        n2 = float(input('welk tweede getal wil je'))
        print(division(n1, n2))
        n1 = division(n1, n2)
    elif choice == 'e':
        n2 = 1
        print(addition(n1, n2))
        n1 = addition(n1, n2)
    elif choice == 'f':
        n2 = 1
        print(subtraction(n1, n2))
        n1 = subtraction(n1, n2)
    elif choice == 'g':
        n2 = 2
        print(multiplication(n1, n2))
        n1 = multiplication(n1, n2)
    elif choice == 'h':
        n2 = 2
        print(division(n1, n2))
        n1 = division(n1, n2)
    elif choice == 'i':
        break







    