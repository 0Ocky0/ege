a = 0
n = 1
while a != 64:
    a ='5' + '2' * n
    while '52' in a or '1122' in a or '2222' in a:
        if '52' in a:
            a = a.replace('52', '11', 1)
        if '2222' in a:
            a = a.replace('2222', '5', 1)
        if '1122' in a:
            a = a.replace('1122', '25', 1)
        n += 1
print(n)