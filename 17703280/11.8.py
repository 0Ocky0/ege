from itertools import *
a = 'КОНФЕТА'
cntr = 0
for i in product(a, repeat = 5):
    if i.count('Е') == 2 and i[1] != 'Ф':
        cntr += 1
        print(i)
print(cntr)
