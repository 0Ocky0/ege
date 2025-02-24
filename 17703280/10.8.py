from itertools import *
cntr = 0
for j in range(1,11):
    for i in permutations('0123456789',j):
        x = ''.join(i)
        if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
            cntr += 1
print(cntr + 1)