for A in range(0, 200):
    f = True
    for x in range(0, 500):
        exp = ((x & 45 > 0) or (x & 89 > 0)) <= (x & A > 0)
        if not exp:
            f = False
            break
    if f:
        print(A)
        break
