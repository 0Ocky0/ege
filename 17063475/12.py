from itertools import *
for b in product('12', repeat=43):
    a = '0' + str(b)
    strok = a
    while '01' in a or '02' in a:
        a = a.replace('02', '1110', 1)
        a = a.replace('01', '220', 1)
    cntr = 0
    aa = ''
    for j in range(len(a)):
        aa += a[j]
    for i in range(int(aa)**0.5 + 1):
        if aa % i == 0:
            cntr += 1
    otv = list(map(int, strok))
    summa = sum(otv)
    if cntr == 0:
        print()