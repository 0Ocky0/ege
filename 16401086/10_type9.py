f = open('999.csv').readlines()
lines = [list(map(int,n.split(','))) for n in f]
cntr = 0
for a in lines:
    if a.count(min(a)) == 1 and len(a) != len(set(a)):
        if max(a) > ((sum(a) - max(a)) // 5) * 3:
            cntr += 1
print(cntr)
