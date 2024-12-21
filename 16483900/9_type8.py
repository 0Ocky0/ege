from itertools import *
cntr =0
for n in product('АЗИМ', repeat = 5):
    if (n.count('А') == 1 and n.count('И') == 0) or (n.count('И') == 1 and n.count('А') == 0):
        cntr += 1
print(cntr)