f = open('zadanie24_1.txt').readline()
f = f.replace('AB', 'X')
print(f)
cntr = 0
maxim = 0
for i in f:
    if i == 'X':
        cntr += 1
    if i != 'X':
        cntr = 0
    maxim = max(cntr, maxim)
print(maxim * 2)