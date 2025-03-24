from itertools import *


def f(x, y, z, w):
    return ((z <= w) or (y == w)) and ((x or z) == y)


for a1, a2, a3, a4 in product([0, 1], repeat=4):
    tabs = [(0, 1, 1, 0), (a1, 1, 0, a2), (0, a3, a4, 1)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [1, 1, 1]:
                print(p)
