f = open('9.csv')
c = 0
for s in f:
    m = [int(x) for x in s.split(',')]
    p3 = [x for x in m if m.count(x) == 3]
    n = [x for x in m if m.count(x) == 1]
    if len(p3) == 3 and len(n) == 3:
        if (sum(p3))**2 > (sum(n))**2:
            c += 1
print(c)