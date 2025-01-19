from itertools import *

cntr = 0
for a in product('АВНРЬЯ', repeat=5):
    bob = ''
    cntr += 1
    bob += a[0]
    bob += a[1]
    bob += a[2]
    bob += a[3]
    bob += a[4]
    if a[0] != 'Я' and a.count('Ь') <= 1 and 'ЯЯ' not in bob:
        print(cntr, a)
