from itertools import *
cntr = 0
a = 'АНДРЕЙ'
for a in product(a, repeat = 6):
    if a.count('А') >= 1 and a.count('Й') <= 1:
        cntr += 1
print(cntr)