from itertools import *


def f(x, y, z, w):
    return ((not (y)) <= (z == w)) and ((z <= x) == w)


for a1, a2 in product([0, 1], repeat=2):
    tabs = [(1, 1, 0, 1), (0, 1, 1, 1), (0, a1, a2, 0)]
    if len(set(tabs)) == len(tabs):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [1, 1, 1]:
                print(p)