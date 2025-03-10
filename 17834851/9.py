f = open('9.csv')
a = [list(map(int, i.split(';'))) for i in f]
cntr = 0
for n in a:
    povt = []
    nep = []
    for b in n:
        if n.count(b) == 2:
            povt.append(b)
        if n.count(b) == 1:
            nep.append(b)
    if len(povt) == 2 and len(nep) == 4:
        if (sum(nep) / len(nep)) < sum(povt):
            cntr += 1
print(cntr)
