f = open('9.csv')

cnt = 0
p = []
for s in f:
    a = list(map(int,s.split(';')))
    a.sort()
    for i in range(len(a)-3):
        if (a[i]==a[i+1] == a[i+2] == a[i+3]) and len(set(a)) == 4:
            p.append(a[i])
            if a[i] < sum(a)/len(a):
                cnt += 1
print(cnt)