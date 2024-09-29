for i in range(1, 1000):
    n = f'{i:b}'
    if i % 2 == 0:
        n = n + '10'
    else:
        n = n + '01'
    if int(n,2) < 102:
        print(i, n, int(n,2))