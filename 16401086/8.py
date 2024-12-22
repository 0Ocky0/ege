from itertools import *
cntr = 0
for a in product('АВЛОР', repeat= 4):
    cntr += 1
    if a[0] == 'Л':
        print(cntr)