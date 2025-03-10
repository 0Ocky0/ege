from itertools import *
cntr = 0
for a in product('БОРИС', repeat = 6):
    if a.count('Б') == 1 and a.count('Р') == 1 and (a.count('С') == 1 or a.count('С') == 0):
        print(a)
        cntr += 1
print(cntr)