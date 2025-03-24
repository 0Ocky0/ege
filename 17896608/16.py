f = open('17 (32).txt')
n = [int(i) for i in f]
otv = []
for a in n:
    for b in n[1:]:
        if (max(a, b) - min(a,b)) % 60 == 0 and (a % 15 == 0 or b % 15 == 0):
            otv.append(max(a, b) - min(a,b))
print(len(otv), max(otv))

