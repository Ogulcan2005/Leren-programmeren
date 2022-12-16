boodschappenlijst = {}
extra_invoegen = "ja"
while extra_invoegen == "ja":
    product = input("Welk product wil je: ")
    aantal = int(input(f"Hoeveel {product} wil je: "))
    if product not in boodschappenlijst:
        boodschappenlijst.update({product : aantal})    
    else:
        boodschappenlijst[product] += aantal
    extra_invoegen = input("Wil je nog een product toevoegen ja/nee: ")
print("----[BOODSCHAPPENLIJST]----")
for k , v in bag.items():
    print(f"{v}x {k}")
print("---------------------------")
