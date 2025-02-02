from itertools import *


def f(x, y, z, w):
    return ((x and y) or (y == z) or w)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tabs = [(a1, 1, 0, 0), (0, a2, 1, a3), (0, 1, a4, 1)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [0, 0, 0]:
                print(p)
