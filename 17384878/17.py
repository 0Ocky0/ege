f = open('17.txt').readlines()
n = [int(i) for i in f]
otv = []
for a, b in zip(n, n[1:]):
    if (a * b) % 15 == 0 and (a + b) % 7 == 0:
        otv.append(a + b)
print(len(otv), max(otv))