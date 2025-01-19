for n in range(3, 10000):
    chis = n
    summer = ''
    chis3 = ''
    while chis > 0:
        chis3 = str(chis % 3) + chis3
        chis = chis // 3
    if n % 3 == 0:
        chis3 = chis3 + chis3[-2:]
    else:
        summ = chis3.count('1') + chis3.count('2') * 2 + chis3.count('3') * 3
        while summ > 0:
            summer = str(summ % 3) + summer
            summ = summ // 3
        chis3 = chis3 + summer
    if int(chis3, 3) > 220:
        print(int(chis3, 3), chis3, n)