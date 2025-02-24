from itertools import *
cntr =0
for a in product('АПРСУ', repeat = 5):
    cntr += 1
    x = ''.join(a)
    if x.count('У') <= 1 and 'АА' not in x:
        print(cntr, x)