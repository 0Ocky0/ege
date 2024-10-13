with open('10(9).csv') as f:
    cnt = 0
    for i in f:
        a = list(map(int, i.split()))
        a.sort()
        if len(a) == len(set(a)) and sum(j % 2 == 0 for j in a) > sum(j % 2 != 0 for j in a) and sum(j for j in a if j % 2 == 0) < sum(j for j in a if j % 2 != 0):
            cnt += 1
print(cnt)
