f = open('17 (28).txt')
n = [int(l) for l in f]
minim = min(n)
maxim = max(n)
ostat = maxim % 3
ost = minim % 3
otv = []
for a, b in zip(n, n[1:]):
    if (a % 3 == ost or b % 3 == ost) and (a % 7 == ostat or b % 7 == ostat):
        otv.append(a + b)
print(len(otv), max(otv))