for n in range(1, 500):
    a = bin(n)[2:]
    summer = a.count('1')
    a = a + str(summer % 2)
    summer = a.count('1')
    a = a + str(summer % 2)
    if int(a, 2) > 93:
        print(int(a,2), a, n)
