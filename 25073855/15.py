for A in range(1, 1000):
    cntr = 0
    for x in range(1, 501):
        for y in range(1, 501):
            if ((x - 3 * y) < A) or (y > 400) or (x > 56):
                cntr += 1
    if cntr == 500 * 500:
        print(A)
        break