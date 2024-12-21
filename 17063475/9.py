f = open('09 (7).csv')
lines = [list(map(int, i.split(','))) for i in f]
count = 0
lines.insert(0, [0, 0, 0, 0, 0, 0, 0, 0])
lines.append([0, 0, 0, 0, 0, 0, 0, 0])
for i in lines:
    i.insert(0, 0)
    i.append(0)
for i in range(1, len(lines) - 1):
    k_i = 0
    for j in range(1, 7):
        if lines[i].count(lines[i][j]) == 1:
            t = lines[i][j]
            if (t < lines[i][j - 1] or t < lines[i][j + 1]
                    or t < lines[i - 1][j - 1] or t < lines[i - 1][j] or t < lines[i - 1][j + 1]
                    or t < lines[i + 1][j - 1] or t < lines[i + 1][j] or t < lines[i + 1][j + 1]):
                k_i += 1
    if k_i >= 3 and len(set(lines[i])) < 7:
        count += 1
print(count)
