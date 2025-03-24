a = '9' * 127
while '333' in a or '999' in a:
    if '333' in a:
        a = a.replace('333', '9', 1)
    if '999' in a:
        a = a.replace('999', '3', 1)
    print(a)