def aantal_bolletjes() -> int:
    hoeveel_bollen = int(input("Hoeveel bolletjes wilt u? "))
    return hoeveel_bollen

def bakje_hoorn(bollen):
    while True:
        if bollen > 0 and bollen < 4:
            bakje_hoorn = input(f"Wilt u deze {bollen} bolletje(s) in een hoorntje of een bakje? ")
            if bakje_hoorn == "bakje":
                print(f"Hier is uw {bakje_hoorn} met {bollen} bolletje(s).")
                break
            elif bakje_hoorn == "hoorn":
                print(f"Hier is uw {bakje_hoorn} met {bollen} bolletje(s).")
                break
            else:
                print("Sorry, dat snap ik niet...")
        elif bollen >= 4 and bollen < 9:
            print(f"Dan krijgt u van mij een bakje met {bollen} bolletjes.")
            print(f"Hier is uw bakje met {bollen} bolletje(s).")
            break

        elif bollen >= 9:
            print("Sorry, zulke grote bakken hebben we niet.")
            bollen = int(input("Hoeveel bolletjes wilt u? "))

        else:
            print("Sorry, dat snap ik niet...")
            bollen = aantal_bolletjes()
