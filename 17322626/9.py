f = open('9.csv')
lines = [list(map(int, i.split(',')))for i in f]
print(lines)
cntr = 0
for i in lines:
    i.sort()
    if i[0] + i[1] < i[2] or i[0] + i[1] < i[3]:
        print(i)
        cntr += 1
print(cntr)