f = open('17.txt')
n = [int(l) for l in f]
otv = []
minim = 100001
for i in n:
    if 99 < i < 1000 and i % 10 == 5:
        minim = min(i, minim)
for a, b in zip(n, n[1:]):
    if ((99 < a < 1000) != (99 < b < 1000)) and ((a + b) % minim == 0):
        otv.append(a + b)
print(len(otv), min(otv))
