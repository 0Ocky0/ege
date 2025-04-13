f = open('17 (33).txt')
n = [int(i) for i in f]
otv = []
for a, b in zip(n, n[1:]):
    if (max(a, b) - min(a, b)) % 36 == 0 and (a % 13 == 0 or b % 13 == 0):
        otv.append(abs(a - b))
print(len(otv), max(otv))