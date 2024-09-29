for i in range(10000, 3, -1):
    s = '0' + str(i) + '0'
a = s
while '00' not in a:
    a = a.replace('01', '220', 1)
    a = a.replace('02', '1013', 1)
    a = a.replace('03', '120', 1)
    if a == '1'*13 + '2'*18:
        print(a)
