for i in range(10000, 100000):
    n = str(i)
    a1 = n[0] + n[2] + n[4]
    a2 = n[1] + n[3]
    if int(a1) < int(a2):
        a = a1 + a2
    else:
        a = a2 + a1
    if int(a) == 723:
        print(i)
        break