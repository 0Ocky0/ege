f = open('9.csv')
n = [list(map(int, i.split(';'))) for i in f]
cntr = 0
for l in n:
    povt = []
    nep = []
    for i in l:
        if int(l.count(l[0]) >= 3) + int(l.count(l[1]) >= 3) + int(l.count(l[2]) >= 3) + int(l.count(l[3]) >= 3) + int(l.count(l[4]) >= 3) + int(l.count(l[5]) >= 3):

            if l.count(i) >= 2:
                povt.append(i)
            if l.count(i) == 1:
                nep.append(i)
    if len(povt) > 0 and len(nep) > 0:
        if sum(povt) / len(povt) > sum(nep) / len(nep):
            cntr += 1
            print(l)
print(cntr)