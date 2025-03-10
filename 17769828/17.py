f = open('17 (30).txt')
n = [int(l) for l in f]
otv = []
for a in range(0, len(n)):
    for b in range(a + 1, len(n)):
        if (max(n[a], n[b]) - min(n[a], n[b])) % 2 == 0 and (n[a] % 31 == 0 or n[b] % 31 == 0):
            otv.append(n[a] + n[b])
print(len(otv), max(otv))