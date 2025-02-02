a = '1' * 99
while '111' in a:
    if '222' in a:
        a = a.replace('222', '1', 1)
    else:
        a = a.replace('111', '2', 1)
    print(a)
