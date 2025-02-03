f = open('26.txt')
n = int(f.readline())
line = [i for i in f.readlines()]
line.sort()
ar = []
for i in line:
    bob = map(int, i.split())
print(ar)