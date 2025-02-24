from itertools import *


def f(x, y, z, w, u):
    return ((z <= w) and (y == (not x))) <= (u == (y or z))


for a1, a2, a3, a4, a5, a6, a7, a8 in product([0, 1], repeat=8):
    tabs = [(0, a1, 0, 0, 0), (0, a2, a3, 0, 0), (a4, 0, 0, 0, a5), (0, 0, a6, a7, a8)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzwu'):
            if [f(**dict(zip(p, r))) for r in tabs] == [0, 0, 0, 0]:
                print(p)
