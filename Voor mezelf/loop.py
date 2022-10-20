from multiprocessing.resource_sharer import stop


x = 0
total = 1
while x <= 10:
    print(x)
    x += 1

for y in range(11):
    print(y)