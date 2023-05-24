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
            zin += ", "
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
# to do: use getItemsValueInGold
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
    return float(round(totaalGoud,2))

##################### M04.D02.O9 #####################
def checkprofit(profit: int) -> bool:
    return profit <= 10
def getInterestingInvestors(investors:list) -> list:
    lijst = []
    for x in investors:
        if checkprofit(x['profitReturn']):
            lijst.append(x)
    return lijst 

# to do use getInterestingInvestors
def getAdventuringInvestors(investors:list) -> list:
    lijst = []
    for x in investors:
        if x['adventuring'] and checkprofit(x['profitReturn']):
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
    lijst = []
    for investor in getInterestingInvestors(investors):
            lijst.append(round(investor['profitReturn'] / 100 * profitGold,2) )
    return lijst

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    totaal = round((profitGold - sum(investorsCuts)) / fellowship,2)
    return totaal



##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []
    donatie = 10

    # haal de juiste inhoud op
    adventuringfriends = getAdventuringFriends(friends)
    interestinginvestors = getInterestingInvestors(investors)
    adventuringinvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold,investors)
    hoeveel_goud =  getAdventurerCut(profitGold, investorsCuts, len(adventuringfriends)+1  + len(adventuringinvestors))
    

    # verdeel de uitkomsten
    for person in people:
        person_cash = person['cash']
        start = getPersonCashInGold(person_cash)
        
        if person == mainCharacter:
            end = start + hoeveel_goud+(donatie*len(adventuringfriends))
        elif person in adventuringfriends:
            end = round((start + hoeveel_goud) - donatie,2)
        else:
            end = start
            
        if "profitReturn" in person:
            if person in interestinginvestors and person in adventuringinvestors:
                    end = (profitGold/100)
                    profit = end * person["profitReturn"]
                    end = profit + start + hoeveel_goud
            elif person in interestinginvestors:
                    end = (profitGold/100)
                    profit = end * person["profitReturn"]
                    end = profit + start
                    
        earnings.append({
            'name'   : person['name'],
            'start'  : start,
            'end'    : end
        })
                                                                                                                                                                                                  
    return earnings

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