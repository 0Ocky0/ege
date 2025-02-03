from itertools import *
a = '0' + '1' * 12 + '2' * 15 + '17' * 3
for l in permutations(a):
    while '01' in l or '02' in l or '03' in l:
        l = l.replace('01', '103', 1)
        l = l.replace('02','10', 1)
        l = l.replace('03', '210', 1)
print(l)
