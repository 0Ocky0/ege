for a in range(500):
    cntr = 0
    for m in range(1, 301):
        for n in range(1, 301):
            if (3 * m + 4 * n > 66) or (m <= a) or (n < a):
                cntr += 1
    if cntr == 300 * 300:
       print(a)
       break
