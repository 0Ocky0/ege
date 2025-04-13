f = open('24.txt')
cntr = 0
for l in f:
    if l.count('E') > l.count('A'):
        cntr += 1
print(cntr)