for a in range(100, 1000):
    a1 = int(str(a)[0]) + int(str(a)[1])
    a2 = int(str(a)[1]) + int(str(a)[2])
    if a1 < a2:
        aa = str(a2) + str(a1)
    else:
        aa = str(a1) + str(a2)
    if aa == '159':
        print(a)