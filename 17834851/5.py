for i in range(100, 1000):
    nn = str(i)
    n1 = int(nn[0]) + int(nn[1])
    n2 = int(nn[1]) + int(nn[2])
    if n1 > n2:
        n = str(n2) + str(n1)
    else:
        n = str(n1) + str(n2)
    if n == '714':
        print(i)
        break
