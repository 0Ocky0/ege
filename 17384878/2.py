from itertools import *


def f(x, y, z, w):
    return (((x and (not (y))) or (w <= z)) == (z == x))


for a1, a2, a3 in product([0, 1], repeat=3):
    tabs = [(a1, 0, 0, 1), (0, 1, 0, 0), (0, a2, a3, 1)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tabs] == [1, 1, 1]:
                print(p)
