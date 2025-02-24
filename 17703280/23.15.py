for a in range(150):
    cntr = 0
    for x in range(1, 151):
        for y in range(1, 151):
            if (x + 2 * y > 48) or (y > x) or (x + 3 * y < a):
                cntr += 1
    if cntr == 150 * 150:
        print(a)
