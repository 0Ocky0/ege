a = '7' * 85
while '333' in a or '777' in a:
    if '333' in a:
        a = a.replace('333', '7', 1)
    else:
        a = a.replace('777', '3', 1)
    print(a)