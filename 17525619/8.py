from itertools import *
cntr = 0
for a in product('УОА', repeat = 6):
    cntr += 1
    print(a)
    if a[0] == 'О' and a[0] == 'О' and a[1] == 'У' and a[2] == 'У' and a[3] == 'У' and a[4] == 'О' and a[5] == 'О':
        print(cntr)
        break