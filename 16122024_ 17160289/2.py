from itertools import *
bob = []
otv = []
def f(x, y, z, w):
    return ((x or (not y)) <= (w == y))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(0, a1, 0, 0), (a2, 1, 1, a3), (a4, 0, 0, 0)]
    # print(tab, len(tab), len(set(tab)))
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in tab] == [0, 0, a5]:
                print(p)
                otv.append(p)
print("---------------------")
def f2(x, y, z, w):
    return ((x or (not y)) == (w <= z))


for a1, a2, a3, a4, a5 in product([0, 1], repeat=5):
    tab = [(0, a1, 0, 0), (a2, 1, 1, a3), (a4, 0, 0, 0)]
    # print(tab, len(tab), len(set(tab)))
    if len(tab) == len(set(tab)):
        for p in permutations('xyzw'):
            if [f2(**dict(zip(p, r))) for r in tab] == [0, a5, 0]:
                print(p)
                bob.append(p)
for i in range (len(max(otv, bob))):
    print(otv[i], bob[i])