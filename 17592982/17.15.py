f = open('17 (25).txt')
n = [int(l) for l in f]
minim = min(n)
maxim = max(n)
otv = []
ost = minim % 5
ostat = maxim % 7
for a, b, c in zip(n, n[1:], n[2:]):
    if (int(len(str(a)) == 4) + int(len(str(b)) == 4) + int(len(str(c)) == 4) >= 1) and (int(a % 5 == ost) + int(b % 5 == ost) + int(c % 5 == ost) < 2) and (int(a % 7 == ostat) + int(b % 7 == ostat) + int(c % 7 == ostat) >= 2):
        otv.append(a + b + c)
print(len(otv), max(otv))
