f = open('9.csv')
lines = [list(map(int, l.split(';'))) for l in f]
cntr = 0
for n in lines:
    if len(n) != len(set(n)):
        if n.count(max(n)) == 1:
            A = [x for x in n if n.count(x) > 1]
            if sum(A) > max(n):
                cntr+= 1
print(cntr)