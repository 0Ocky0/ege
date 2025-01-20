from itertools import *
cntr = 0
for a in product('0123456', repeat = 4):
    if a[0] > a[1] and a[1] > a[2] and a[2] > a[3]:
        cntr += 1
print(cntr)