f = open('17 (27).txt')
n = [int(l) for l in f]
minim = min(n)
maxim = max(n)
otv = []
ost = maxim % 7
ostat = minim % 3
for a, b in zip(n, n[1:]):
    if ((int(a % 3 == ostat)) + (int(b % 3 == ostat)) >= 1) and ((int(a % 7 == ost)) + (int(b % 7 == ost)) >= 1):
        otv.append(a + b)
print(len(otv), max(otv))