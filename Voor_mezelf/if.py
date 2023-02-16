# Vraag: console of pc
# bereken de prijs pc: 45 euro
# console: 55 euro
membership_korting = 15
platform = input('Ben je een pc of console gamer')
prijs = 45

if platform == 'console':
    prijs = 55
    if input('bent u een member') == 'ja':
     prijs = 55 - membership_korting
    

if platform == 'pc':
    prijs = 45

print(f'U bent {platform} gamer, dan kost de game: {prijs} Euro')