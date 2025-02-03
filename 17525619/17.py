f = open('17_2024.txt')
n = [int(lines) for lines in f]
maxim = 0
otv = []
for i in n:
    if i % 100 == 13:
        maxim = max(i, maxim)
for a, b, c in zip(n, n[1:], n[2:]):
    if int(len(str(a)) == 3) + int(len(str(b)) == 3) + int(len(str(c)) == 3) == 2 and a + b + c < maxim:
        otv.append(a + b + c)
print(len(otv), max(otv))