f = open('99.txt')
count = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if len(a) == len(set(a)):
        sr1 = (a[0] + a[-1])/2
        sr2 = (sum(a) - a[-1] - a[0]) / 4
        if sr1 > sr2:
            count += 1
print(count)