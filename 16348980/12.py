for n in range(3, 10000):
    a = '5' + '2' * n
    while '52' in a or '2222' in a or '1122' in a:
        a = a.replace('52', '11', 1)
        a = a.replace('2222', '5', 1)
        a = a.replace('1122', '25', 1)
    if a.count('1') + a.count('2') * 2 + a.count('5') * 5 == 64:
        print(n)