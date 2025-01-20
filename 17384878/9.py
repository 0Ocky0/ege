f = open('9.csv')
lines = [list(map(int, l.split(';'))) for l in f]
cntr = 0
for n in lines:
    if int(n.count(n[0]) == 2) + int(n.count(n[1]) == 2) + int(n.count(n[2]) == 2) + int(n.count(n[3]) == 2) + int(n.count(n[4]) == 2) + int(n.count(n[5]) == 2) + int(n.count(n[6]) == 2) == 4 and int(n.count(n[0]) == 1) + int(n.count(n[1]) == 1) + int(n.count(n[2]) == 1) + int(n.count(n[3]) == 1) + int(n.count(n[4]) == 1) + int(n.count(n[5]) == 1) + int(n.count(n[6]) == 1) == 3:
        cntr += 1
        print(n)
print(cntr)