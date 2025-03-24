from itertools import *
cntr = 0
for a in product('ЗИМА', repeat = 5):
    a = ''.join(a)
    if (a[0] == 'И' or a[0] == 'А') and (a[-1] == 'И' or a[-1] == 'А'):
        cntr += 1
print(cntr)