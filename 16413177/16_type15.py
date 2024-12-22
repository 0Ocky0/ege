for A in range(300):
    k = 0
    for x in range(300):
        for y in range(300):
            if (3 * x + 5 * y < A) or (x >= y) or (y > 8):
                k += 1
    if k == 90_000:
        print(A)
        break