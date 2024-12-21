from itertools import *


def f(x, y, z, w):
    return ((y or z) <= (z and w)) == (not ((x and z) <= (w or y)))

for a1, a2 in product([0,1], repeat = 2):
    tabs =[(a1,1,1,1), (0,0,0,a2), (1,1,0,0)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p,r))) for r in tabs] == [1,1,1]:
                print(p)