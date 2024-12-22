from itertools import *


def f(x, y, z):
    return ((x or y) <= (y==z))

for a1, a2, a3 in product([0,1], repeat = 3):
    tab = [(0, 0, a1), (0, a2, a3)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p,r))) for r in tab] == [0, 0]:
                print(p)