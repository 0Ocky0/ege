for a in range(500):
    cntr = 0
    for x in range(500):
        for y in range(500):
            if ((3*x + 4*y) != 60) or ((a >= x) and (a >= y)):
                cntr += 1
    if cntr == 500 * 500:
        print(a)
        break
