f = open('../16413177/99.csv')
cnt = 0
for i in f:
    a = list(map(int,i.split(',')))
    if len(a) != len(set(a)):
        sr1 = 0
        k1 = 0
        sr2 = 0
        k2 = 0
        for j in range (0,len(a)):
            if a.count(a[j]) == 1:
                sr1 += a[j]
                k1 += 1
            else:
                sr2 += a[j]
                k2 += 1
        if k1!=0 and k2!=0:
            if (sr1/k1)>(sr2/k2):
                cnt += 1
print(cnt)