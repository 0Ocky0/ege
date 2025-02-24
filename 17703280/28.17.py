f = open('17 (28).txt')
n = [int(l) for l in f]
minim = min(n)
maxim = max(n)
ostat = maxim % 3
ost = minim % 3
otv = []
maxim = 0
for a in n:
    if a % 1000 == 538:
        maxim = max(a, maxim)
for a, b, c, d in zip(n, n[1:], n[2:], n[3:]):
    if (int(len(str(a)) == 5) + int(len(str(b)) == 5) + int(len(str(c)) == 5) + int(len(str(d)) == 5)) >= 2 and (
            int(len(str(a)) != 5) + int(len(str(b)) != 5) + int(len(str(c)) != 5) + int(len(str(d)) != 5)) >= 1:
        if int(a % 3 == 0) + int(b % 3 == 0) + int(c % 3 == 0) + int(d % 3 == 0) > int(a % 7 == 0) + int(
                b % 7 == 0) + int(c % 7 == 0) + int(d % 7 == 0):
            if (a + b + c + d > maxim) and (a + b + c + d < maxim * 2):
                otv.append(a + b + c + d)
print(len(otv), max(otv))
