f = open('09.txt')
count = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if len(a) != len(set(a)):
        if a.count(a[-1]) == 1:
            suma = a[-1]
            sr = ((sum(a) - max(a)) / 5) * 3
            if suma > sr:
                count += 1
print(count)
