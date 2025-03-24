from itertools import *
cntr = 0
for a in product('ABCDX', repeat = 4):
    a = ''.join(a)
    if a.count('X') == 1:
        cntr += 1
print(cntr)