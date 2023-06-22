def bestel_ijs():
    while True:
        aantal = int(input("Hoeveel bolletjes wilt u? "))
        
        if aantal >= 1 and aantal <= 3:
            while True:
                keuze = input(f"Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje? ")
                if keuze == "hoorn":
                    print(f"Hier is uw hoorntje met {aantal} bolletje(s).")
                    break
                elif keuze == "bakje":
                    print(f"Hier is uw bakje met {aantal} bolletje(s).")
                    break
                else:
                    print("Sorry, dat snap ik niet...")
            break
        elif aantal > 3 and aantal <= 8:
            print(f"Dan krijgt u van mij een bakje met {aantal} bolletjes.")
            break
        elif aantal > 8:
            print("Sorry, zulke grote bakken hebben we niet.")
        elif aantal != int:
            print("Sorry, dat snap ik niet...")


bestel_ijs()



    