def f(x):
    if x == 1:
        return False
    for j in range(2, x // 2 + 1):
        if x % j == 0:
            return False
    return True


for n in range(100, 200):
    s = '0' + '1' * n + '2' * n + '0'
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if f(summa):
        print(n)