from itertools import *
a = ['.64', '2.16', '16', '8.32']
for i in permutations(a):
    print(*i)