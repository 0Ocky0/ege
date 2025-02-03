for a in range(500):
    cntr = 0
    for x in range(500):
        for y in range(500):
            if ((y + 2 * x) != 48) or (a < x) or (a < y):
                cntr += 1
    if cntr == 500 * 500:
        print(a)
