# lijst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# lijst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
# print(len(lijst))
# print(lijst)
# lijst2.sort(reverse = True)
# print(lijst2)
# som = 36 + 19 + 27 + 3 + 25
# print(som)
# print('element nummer van 25 is 25')
# lijst3 = [1,'aap', 2,'apen', 3,'watermeloen', 15, 27]
# int(lijst3)
# print(lijst3)
# lijst = [5, 12, 19, 27, 3]
# lijst.append(25)
# lijst.remove(12)
# lijst.pop(0)
# lijst.insert(0, 36)
# print(len(lijst))
# print(lijst)

teller = 0
lijst2 = [1,'aap', 2,'apen', 3,'watermeloen', 15, 27]
for e in lijst2:
    typ = str(type(e))
    if typ == "class 'int>'":
        teller += 1
print(teller)
