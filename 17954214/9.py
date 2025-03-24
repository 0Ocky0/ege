f = open('9.csv')
line = [list(map(int, l.split(';'))) for l in f]
for n in line:
    