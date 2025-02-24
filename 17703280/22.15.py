for a in range(500):
    cntr = 0
    for x in range(1, 301):
        for t in range(1, 301):
            if ((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0):
                cntr += 1
    if cntr == 300 * 300:
        print(a)