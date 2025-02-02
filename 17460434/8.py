from itertools import *
cntr = 0
for a in product('0ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat = 7):
    print(a)
    cntr += 1
    if a[0] == '0' and a[1] == 'F' and a[2] == 'D' and a[3] == 'E' and a[4] == 'C' and a[5] == 'B' and a[6] == 'A':
        print(cntr)
        break