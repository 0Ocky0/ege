from itertools import *


def f(x, y, z, w):
    return (x <= (y <= z)) and (y <= (z == (not w)))


for a1, a2, a3, a4, a5, a6 in product([0, 1], repeat=6):
    tabs = [(0, 0, a1, 0), (0, 0, a2, a3), (a4, 0, a5, a6)]
    if len(tabs) == len(set(tabs)):
        for p in permutations('xyzw'):
           if [f(**dict(zip(p,r))) for r in tabs] == [0, 0, 0]:
               print(p)