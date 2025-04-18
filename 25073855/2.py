from itertools import *


def f(x, y, z, w):
    return (not((not(x) or y) and not(w)) or not(z and not(y and w)))


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat=7):
    tabs = [(0, a1, a2, 1), (a3, 1, a4, a5), (1, 0, a6, a7)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [0, 0, 0]:
                print(p)
