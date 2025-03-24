# from math import *
# otv = []
# for i in range(4500, 5001):
#     for j in range(2, ceil(i ** 0.5)+ 1):
#         delit = 0
#         if i % j == 0 and j % 2 == 1:
#             delit += 1
#     if delit == 5:
#         otv.append(i)
# print(otv)
for i in range(45000000,50000001):
    a = []
    z = 1
    while i % 2 == 0:
        i = i//2
    if (i ** 0.25) == int(i ** 0.25):
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                if j % 2 == 1:
                    a.append(j)
                    if (i//j) % 2 == 1:
                        a.append(i//j)
                if len(a) >= 4:
                    break
        z = len(set(a)) + 1
        if i % 2 == 1:
            z += 1
    if z == 5:
        print(i)