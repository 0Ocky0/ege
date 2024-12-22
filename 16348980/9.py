f = open('09 (8).csv').readlines()
count = 0
lines = [list(map(int,lines.split(','))) for lines in f]
for i in lines:
    if len(i) != len(set(i)):
            if i.count(max(i)) == 1:
                A = [x for x in i if i.count(x) > 1]
                if sum(A) > max(i):
                    count += 1
print(count)