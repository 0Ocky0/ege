from itertools import *


def f(x, y, z, w):
    return (((x or (not(y))) and ((not(z))==w)) <= (y and z))

for a1, a2, a3, a4 in product([0,1], repeat = 4):
    tab = [(1, a1, 1, 1), (0, 0, a2, 0), (0, a3, a4, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in tab] == [0, 0, 0]:
                print(p)