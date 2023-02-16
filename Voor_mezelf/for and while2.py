teller = 0 
antwoord = " "

while antwoord != "stop":
    antwoord = input('voer stop in om te stoppen')
    teller += 1
    print(teller)
print(f'aantal enters: {teller}')