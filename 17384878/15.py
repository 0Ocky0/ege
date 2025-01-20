for A in range(5000):
    cntr = 0
    for x in range(300):
        for y in range(300):
            if (x*y<A) or (y > x) or (x >= 8):
                cntr += 1
    if cntr == 300 * 300:
        print(A)
        break
