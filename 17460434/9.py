f = open('9 .csv')
lines = [list(map(int, l.split(';'))) for l in f]
cntr = 0
for n in lines:
    if max(n) > n[0] + n[1] +n[2] - max(n):
        cntr += 1
        print(n)
print(cntr)