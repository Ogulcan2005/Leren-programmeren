import time
from termcolor import colored
from data import *
import math
##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount/10

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    return amount/50

def platinum2gold(amount:int) -> float:
    return amount * 25


def getPersonCashInGold(personCash:dict) -> float:
    copper = copper2gold(personCash['copper'])
    silver = silver2gold(personCash['silver'])
    gold = personCash['gold']
    platinum = platinum2gold(personCash['platinum'])
    return platinum + gold + silver + copper

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    koste_persoon = people * JOURNEY_IN_DAYS * COST_FOOD_HUMAN_COPPER_PER_DAY
    koste_paard = horses * JOURNEY_IN_DAYS * COST_FOOD_HORSE_COPPER_PER_DAY
    totaal = koste_paard + koste_persoon
    return copper2gold(totaal)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for x in list:
        if key in x:
           if x[key] == value:
               lijst.append(x)
    return lijst 

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people/2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people/3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    paard_koste_per_dag = horses * silver2gold(COST_HORSE_SILVER_PER_DAY) * JOURNEY_IN_DAYS
    tent_koste_per_week = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    totale_koste_in_goud = (paard_koste_per_dag + tent_koste_per_week)
    return totale_koste_in_goud

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    zin = ""
    for x in items:
        if zin != "":
            zin += f", {x['amount']}{x['unit']} {x['name']}"
        else:
            zin += f"{x['amount']}{x['unit']} {x['name']}"
    return zin


def getItemsValueInGold(items:list) -> float:
    prijs_in_goud = 0
    for x in items:
        if x['price']['type'] == "copper":
            prijs_in_goud += copper2gold(x['price']['amount'] * x['amount'])
        elif x['price']['type'] == "silver":
            prijs_in_goud += silver2gold(x['price']['amount']* x['amount'])
        elif x['price']['type'] == "gold":
            prijs_in_goud += x['price']['amount'] * x['amount']
        elif x['price']['type'] == "platinum":
            prijs_in_goud += platinum2gold(x['price']['amount'] * x['amount'])
    return round(prijs_in_goud,2)

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totaalGoud = 0
    for goud in people:
        if goud['cash']['platinum'] > 0:
            totaalGoud += platinum2gold(goud['cash']['platinum'])
        if goud['cash']['gold'] > 0:
            totaalGoud += goud['cash']['gold']
        if goud['cash']['silver'] > 0:
            totaalGoud += silver2gold(goud['cash']['silver'])
        if goud['cash']['copper'] > 0:
            totaalGoud += copper2gold(goud['cash']['copper'])
    return round(totaalGoud,2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    lijst = []
    for x in investors:
        if x['profitReturn'] <= 10:
            lijst.append(x)
    return lijst 


def getAdventuringInvestors(investors:list) -> list:
    lijst = []
    for x in investors:
        if x['adventuring'] and x['profitReturn'] <= 10:
            lijst.append(x)
    return lijst
    
def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    totaal = 0
    aantal_investors = getAdventuringInvestors(investors)
    for x in range(len(aantal_investors)):
        totaal += getItemsValueInGold(gear)
    totaal += getTotalRentalCost(len(aantal_investors), len(aantal_investors))
    totaal += getJourneyFoodCostsInGold(len(aantal_investors),len(aantal_investors))
    return totaal

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    paard = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    mens = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    totaal = int(leftoverGold/(paard + mens))
    return totaal

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    paard_koste = horses * copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * nightsInInn
    mens_koste = people * silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * nightsInInn
    return round(paard_koste + mens_koste,2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    cut_lijst = []
    for investors in getInterestingInvestors(investors):
        investor = round(investors['profitReturn'] / 100 * profitGold,2)
        cut_lijst.append(investor)
    return cut_lijst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    totaal = round((profitGold - sum(investorsCuts)) / fellowship,2)
    return totaal



##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()