for n in range(1, 100):
    b = f'{n:b}'
    if b.count('1') % 2 != 0:
        b += '10'
    else:
        b += '00'
    if int(b,2) > 97:
        print(int(b,2), n)