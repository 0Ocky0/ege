cntr = 0
for i in range(100, 1000000000000):
    a = bin(i)[2:]
    a += bin(int(a)%3)[2:]
    a += bin(int(a)%5)[2:]
    if int(a, 2) > 1111111110 and int(a, 2) < 1444444416:
        cntr += 1
print(cntr)