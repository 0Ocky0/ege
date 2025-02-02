for i in range(3, 200):
    n = bin(i)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)
    if int(n, 2) > 123:
        print(int(n,2), i)
        break
