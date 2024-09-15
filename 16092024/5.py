for n in range(1, 100):
    bobr = f'{n:bobr}'
    if bobr.count('1') % 2 != 0:
        bobr += '10'
    else:
        bobr += '00'
    if int(bobr,2) < 100:
        print(int(bobr,2), n)