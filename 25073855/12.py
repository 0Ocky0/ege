for n in range(4, 10000):
    strok = '1' + '2' * n
    while '12' in strok or '322' in strok or '222' in strok:
        if '12' in strok:
            strok = strok.replace('12','2', 1)
        if '322' in strok:
            strok = strok.replace('322', '21', 1)
        if '222' in strok:
            strok = strok.replace('222', '3', 1)
    if strok.count('1') + strok.count('2') * 2 + strok.count('3') * 3 == 15:
        print(strok, n)
        break