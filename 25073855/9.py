f = open('9.csv')
lines = [list(map(int, l.split(';'))) for l in f]
cntr = 0
for n in lines:
    cntr += 1
    summer = 0
    edin = 0
    if int(n.count(n[0]) == 3) + int(n.count(n[1]) == 3) + int(n.count(n[2]) == 3) + int(n.count(n[3]) == 3) + int(
            n.count(n[4]) == 3) + int(n.count(n[5]) == 3) + int(n.count(n[6]) == 3) == 6:
        # print(n)
        if n.count(n[0]) > 1:
            summer += n[0]
        if n.count(n[0]) == 1:
            edin += n[0]
        if n.count(n[1]) > 1:
            summer += n[1]
        if n.count(n[1]) == 1:
            edin += n[1]
        if n.count(n[2]) > 1:
            summer += n[2]
        if n.count(n[2]) == 1:
            edin += n[2]
        if n.count(n[3]) > 1:
            summer += n[3]
        if n.count(n[3]) == 1:
            edin += n[3]
        if n.count(n[4]) > 1:
            summer += n[4]
        if n.count(n[4]) == 1:
            edin += n[4]
        if n.count(n[5]) > 1:
            summer += n[5]
        if n.count(n[5]) == 1:
            edin += n[5]
        if n.count(n[6]) > 1:
            summer += n[6]
        if n.count(n[6]) == 1:
            edin += n[6]
        if summer // 6 < edin:
            print(cntr)

