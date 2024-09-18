cntr = 0
for s in range(1000, 10000):
    a1 = s//1000 + s // 100 % 10
    a2 = s % 100 // 10 + s % 10
    if a1 > a2 and str(a2) + str(a1) == '616':
        cntr += 1
    elif a2 > a1 and str(a1) + str(a2) == '616':
        cntr += 1
print(cntr)

"""
1 - 11
2 - yzwx
5 - 7
6 - 39
14 - 4
"""