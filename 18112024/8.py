from itertools import *
cntr = 0
for i in product('01A', repeat=8):
    print(i)
    x = ''.join(i)
    if x[0] != '0' and x.count('0') == 2 and x.count('A') <= 4:
        cntr += 6**x.count('A') * 9**x.count('1')
print(cntr)