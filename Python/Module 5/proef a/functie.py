def aantal_bolletjes() -> int:
    hoeveel_bollen = int(input("Hoeveel bolletjes wilt u \n"))
    return hoeveel_bollen
    
bollen = aantal_bolletjes

def bakje_hoorn(bollen):
    if bollen > 0 and bollen < 4:
        bakje_hoorn = input(f"Wilt u deze {bollen} bolletje(s) in een hoorntje of een bakje? ")
        if bakje_hoorn == "bakje":
            print(f"Hier is uw {bakje_hoorn} met {bollen} bolletje(s)")
        elif bakje_hoorn == "hoorn":
            print(f"Hier is uw {bakje_hoorn} met {bollen} bolletje(s)")
        else:
            print("Sorry, dat snap ik niet...")
            bakje_hoorn = input(f"Wilt u deze {bollen} bolletje(s) in een hoorntje of een bakje? ")
    elif bollen > 3 and bollen < 9:
        print(f"Dan krijgt u van mij een bakje met {bollen} bolletjes")
        print(f"Hier is uw bakje met {bollen} bolletje(s).")
    elif bollen > 8:
        print("Sorry, zulke grotebakken hebben we niet")
        bollen = int(input("Hoeveel bolletjes wilt u "))
    elif bollen != int:
        print("Sorry, dat snapik niet...")
        aantal_bolletjes
