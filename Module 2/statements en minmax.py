#input en if-statement
a = int(input('getal a'))
b = int(input('getal b'))

if a > b:
    print('a is meer dan b') 
    max = a
if a < b:
    print('b is meer dan a')
    max = b
################################################
#elif-statement
a = int(input('getal a'))
b = int(input('getal b'))

if (a > b):
    print('b is het kleinste getal')
    min = b 
elif(a < b):
    print('a is het kleinste getal')
    min = a
#####################################################
# else-statement
if (a > b):
    print('b is het kleinste getal')
else:
    print('a en b zijn even groot')
#####################################
#Min en Max
print('Het minimum is: ’ gevolgd door de waarde van Min')
print('Het maximum is: ’ gevolgd door de waarde van Max')
   
