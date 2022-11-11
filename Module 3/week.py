dagen = ('ma', 'di', 'wo', 'do', 'vr', 'za', 'zo')
dagen_v_week = input('Tot welke dag moet ik printen van ma t/m zo')
dag_nr = 0

while dag_nr < 8:
    if dagen[dag_nr] == dagen_v_week:
        break
    print(dagen[dag_nr])
    print(dag_nr)
    dag_nr += 1








# x = int(input('welke dag wilt u dag 1 t/m 7'))
# while x < 8:
#     if x == 1:
#         print('maandag')
#         break
#     elif x == 2:
#         print('dinsdag')
#         break
#     elif x == 3:
#         print('woensdag')
#         break
#     elif x == 4:
#         print('donderdag')
#         break
#     elif x == 5:
#         print('vrijdag')
#         break
#     elif x == 6:
#         print('zaterdag')
#         break
#     elif x == 7:
#         print('zondag')
#         break