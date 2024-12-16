f = open('111.txt')
k = 0
for i in f:
    a=list(map(int,i.split()))
    if len(set(a)) == 4:
        suma = 0
        for j in range (0,len(a)):
            if a.count(a[j])==3:
                suma += a[j]
        if suma**2 > (sum(a)-suma)**2:
            k += 1
print(k)