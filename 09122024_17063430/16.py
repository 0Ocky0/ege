for A in range(0, 10000000):
    for x in range(0,99999):
        exp = ((x & 42 != 0) or (x & 13 != 0)) <= ((x & 30 == 0) <= (x & A != 0))
        if not exp:
            break
    else:
        print(A)
        break
