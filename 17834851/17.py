f = open('17 (31).txt')
n = [int(l) for l in f]
maxim = 0
otv = []
for i in n:
    if i % 1000 == 321:
        maxim = max(i, maxim)
for a, b, c in zip(n, n[1:], n[2:]):
    if int(len(str(a)) == 5) + int(len(str(b)) == 5) + int(len(str(c)) == 5) == 2:
        if int(a % 5 == 0) + int(b % 5 == 0) + int(c % 5 == 0) >= 1:
            if a + b + c > maxim:
                otv.append(a + b + c)
print(len(otv), max(otv))

