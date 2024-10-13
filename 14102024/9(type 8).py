from itertools import *
a = []
for i in product('012345678', repeat = 5):
    if i[0] != '0' and int(i[0]) > int(i[1]) > int(i[2]) > int(i[3]) > int(i[4]):
        a.append(i)
print(len(a))
