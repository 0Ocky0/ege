for a in range(300):
    cntr = 0
    for x in range(300):
        for y in range(300):
            if (x * y < a) or (x < y) or (x >= 12):
                cntr += 1
    if cntr == 300 * 300:
        print(a)
        break
