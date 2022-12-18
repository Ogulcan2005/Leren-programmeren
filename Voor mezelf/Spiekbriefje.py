# # commentaar
# #################################
# waar_of_niet_waar = # boolean
# ######################
# # integer = geheel getal zonder comma 
# # voorbeeld
# aantal = 3
# ###############################################
# # string = een zin of woord
# # voorbeeld
# omschrijving = 'Croky naturel 300gr'
# ######################################
# # float = een cijfer achter de comma
# stuksprijs = 0.89
# #######################################
# # built in functies
# #######################################
# print(str(aantal) + ' '+ omschrijving + " " + str(stuksprijs))
# print (f"{aantal} {omschrijving} {stuksprijs}")
# ######################################################
# multiline_zin = f"""Voor {aantal_pannenkoeken} heb je nodig:
# {bloem/20*aantal_pannenkoeken} gram bloem
# {eieren/20*aantal_pannenkoeken} eieren
# {melk/20*aantal_pannenkoeken} melk ml
# {zout/20*aantal_pannenkoeken} zout
# {boter/20*aantal_pannenkoeken} boter gram"""
# print(multiline_zin)
# #######################################################
# getal = 3

# if (getal == 3):
#     (y == 5)
#     if y == 6:
#         z = 3
#     print('y = 5')
# ##############################################
# # functies
# # input is een build in functie
# def vraagr_een_getal(vraag: str) -> int: #betekent definieer = maak aan 
#     while True:
#         try:  
#             getal = int(input(vraag))
#             break
#         except ValueError:
#             print('je moet een getal invoeren')
#             continue
#     return getal

# leeftijd = vraagr_een_getal('voer u leeftijd in')
# geboorte_jaar = vraagr_een_getal('voer je geboorte jaar in')
# geboorte_maand = vraagr_een_getal('voer je geboorte maand in')
# geboorte_dag = vraagr_een_getal('voer je geboorte dag in')

# print(leeftijd)
# print(geboorte_jaar)

# while True:
#     try:  
#         geboorte_jaar = int(input('voer u leeftijd in'))
#         break
#     except ValueError:
#         print('je moet een getal invoeren')
#         continue

def stel_vraag_return_antwoord_return(vraag: str) -> str:
    antwoord = input(vraag).lower()
    return antwoord
print(stel_vraag_return_antwoord_return('wat wil je typen'))
    