from itertools import *
cntr = 0
for a in permutations('ОЛЬГА'):
    a = ''.join(a)
    if a[0] != 'Ь' and 'ОЬ' not in a and 'АЬ' not in a:
        cntr += 1
print(cntr)