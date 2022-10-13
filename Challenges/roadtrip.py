bottles = 100
pass_around = 1
total = 1
while bottles > 0:
    bottles -= 1
    print(f'{bottles} bottles of beer on the wall, {bottles - pass_around} bottles of beer. Take one down and pass it around, {bottles - total} bottles of beer on the wall')

print(f'No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.')