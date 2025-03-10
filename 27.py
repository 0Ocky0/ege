# f = open('27-B (1).txt')
# s = f.readlines()
# a1 = []
# a2 = []
# a0 = []
# maxim = 9999999999
# for i in s:
#     if int(i) % 3 == 0:
#         a0.append(int(i))
#     if int(i) % 3 == 1:
#         a1.append(int(i))
#     if int(i) % 3 == 2:
#         a2.append(int(i))
# a0.sort()
# a1.sort()
# a2.sort()
# for n in range(24):
#     if a1[0] + a1[1] + a1[2] < maxim:
#         maxim = a1[0] + a1[1] + a1[2]
#     if a2[0] + a2[1] + a2[2] < maxim:
#         maxim = a2[0] + a2[1] + a2[2]
#     if a0[0] + a0[1] + a0[2] < maxim:
#         maxim = a0[0] + a0[1] + a0[2]
#     if a0[0] + a1[0] + a2[0] < maxim:
#         maxim = a0[0] + a1[0] + a2[0]
# print(a0)
# print(a1)
# print(a2)
# print(maxim)

# from itertools import *
#
# # f = open('27-A (1).txt')
# # s = f.readlines()
# # mi = 999999999
# # for p in combinations(s, 3):
# #     sus = sum(map(int,p))
# #     if sus % 3 and sus < mi:
# #         mi = sus
# #         print(mi)