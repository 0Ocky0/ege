f = open('107_17.txt')
n = [int(i) for i in f]
minim = 10**8
otv = []
for i in n:
    if i % 21 == 0:
        minim = min(minim, i)
for a, b in zip(n, n[1:]):
    if a % minim == 0 or b % minim == 0:
        otv.append(a + b)
print(len(otv), max(otv))