function getNumberOfCharacters(text: str) -> int:
    count = 0
    for x in text:
        if x.isalpha():
            count += 1
    return count

function getNumberOfSentences(text: str) -> int:
    teller = 0
    if '.' in text:
        for x in text:
            teller += x.count('.')
    if '?' in text:
        for x in text:
            teller += x.count('?')
    if '!' in text:
        for x in text:
            teller += x.count('!')
    return teller

function getNumberOfWords(text: str) -> int:
    x = text.split()
    return len(x)

function aviScore(){
    let score = 0
    if (getNumberOfWords(text) <= 7.4){
        score = 5
    }
    else if (getNumberOfWords(text) >= 7.5 && getNumberOfWords(text) <= 8.4){
        score = 6
    } 
    else if (getNumberOfWords(text) >= 8.4 && getNumberOfWords(text) <= 9.4){
        score = 7
    }
    else if (getNumberOfWords(text) >= 9.4 && getNumberOfWords(text) <= 10.4){
        score = 8
    }
    else if (getNumberOfWords(text) >= 10.4 && getNumberOfWords(text) <= 11.4){
        score = 11
    }
    else if (getNumberOfWords(text) > 11){
        score = 12
    }
    return score
}
