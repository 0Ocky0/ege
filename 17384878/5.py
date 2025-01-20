for i in range(3, 100):
    n = bin(i)[2:]
    a = n[::-1]
    while a[0] == 0:
        if a[0] == 0:
            a = a[1:]
    if int(a, 2) == 13:
        print(i, a, int(a, 2))
