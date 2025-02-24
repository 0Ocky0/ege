from itertools import *


def f(x, y, z, w):
    return ((x <= y) <= z) or (not w)


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tabs = [(a1, 0, a2, 0), (1, a3, a4, a5), (0, 1, a6, a7)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [0, 0, 0]:
                print(p)
