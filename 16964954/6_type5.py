bob = [0]*10000
for i in range(1,1000):
    a = bin(i)[2:]
    a = a + bin(i % 4)[2:]
    otv = int(a, 2)
    bob[otv] = 1
maxim = 0
for i in range(100000):
    maxim = max(maxim, sum(bob[i : i + 65]))
print(maxim)