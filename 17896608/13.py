a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:13]:
    otv = int(f'4C{x}4', 15) + int(f'{x}62A', 13)
    if otv % 121 == 0:
        print(otv // 121)