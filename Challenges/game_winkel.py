spelletje = 24.95 /100 * 60
hoeveel_games = int(input('hoeveel games wilt u '))
leverancier_kosten = 1 + ((hoeveel_games - 1) * 0.25)
spelletje_totaal = spelletje * hoeveel_games
print(leverancier_kosten + spelletje_totaal)
        

