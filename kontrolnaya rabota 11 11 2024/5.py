for N in range(0, 9999999999):
    R = bin(N)[2:]
    if N % 5 == 0:
        R = R + bin(5)[2:]
    else:
        R = R + '1'
    if int(R,2) % 7 == 0:
        R = R + bin(7)[2:]
    else:
        R = R + '1'
    if int(R, 2) < 1728404:
        print(N, R, int(R, 2))


