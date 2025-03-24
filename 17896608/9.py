f = open('9.csv')
n = [list(map(int, i.split(';'))) for i in f]
cntr = 0
for l in n:
    zamet_chet = []
    zamet_nechet = []
    nezamet_chet = []
    nezamet_nechet = []
    for i in l:
        if i > sum(l) / len(l):
            if i % 2 == 0:
                zamet_chet.append(i)
            else:
                zamet_nechet.append(i)
        else:
            if i % 2 == 0:
                nezamet_chet.append(i)
            else:
                nezamet_nechet.append(i)
    if len(zamet_chet) > len(zamet_nechet):
        if sum(zamet_chet) + sum(nezamet_chet) < sum(nezamet_nechet) + sum(zamet_nechet):
            cntr += 1
print(cntr)
