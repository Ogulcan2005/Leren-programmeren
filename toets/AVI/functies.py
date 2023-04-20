EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    count = 0
    for x in text:
        if x.isalpha():
            count += 1
    return count
# opdracht 2
def getNumberOfSentences(text: str) -> int:
    teller = 0
    for x in text:
        if x in '.?!':
            teller += 1
    return teller
# opdracht 3
def getNumberOfWords(text: str) -> int:
    x = text.split()
    return len(x)
# opdracht 5
def aviScore(text: str) -> int:
    score = 0
    gemiddelde = getNumberOfWords(text) / getNumberOfSentences(text)
    if gemiddelde <= 7.4:
        score = 5
    elif gemiddelde > 7.4 and gemiddelde <= 8.4:
        score = 6
    elif gemiddelde > 8.4 and gemiddelde <= 9.4:
        score = 7
    elif gemiddelde > 9.4 and gemiddelde <= 10.4:
        score = 8
    elif gemiddelde > 10.4 and gemiddelde <= 11.4:
        score = 11
    elif gemiddelde > 11:
        score = 12
    return score

