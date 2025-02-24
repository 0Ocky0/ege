from itertools import *
cntr = 0
for a in product('АГЛОЬ', repeat = 5):
    cntr += 1
    x = ''.join(a)
    if x == 'ОЛЬГА':
        print(x, cntr)