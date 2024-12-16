for i in range(1, 999999):
    a = '0' + str(i) + '0'
    while '00' not in a:
        a = a.replace('01', '220', 1)
        a = a.replace('02', '1013', 1)
        a = a.replace('03', '120', 1)
    if a.count('1') == 13 and a.count('2') == 18:
        print(a, i)
        break