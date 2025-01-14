from itertools import *


def f(x, y, z, w):
    return ((z == (x <= w)) and (x == (not (w <= y))))


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tabs = [(0, a1, 0, 0), (a2, a3, 0, 0), (1, 1, a4, 0)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [1, 1, 0]:
                print(p)
