cntr = 0
for i in range(100, 1000):
    n = str(i)
    a1 = int(n[0]) + int(n[1])
    a2 = int(n[1]) + int(n[2])
    if a1 <= a2:
        otv = str(a1) + str(a2)
    else:
        otv = str(a2) + str(a1)
    if otv == '1216':
        cntr += 1
print(cntr)