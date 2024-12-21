f = open('09 (8).csv').readlines()
lines = [list(map(int,lines.split(','))) for lines in f]
print(lines)