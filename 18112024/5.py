for N in range(456789014, 0, -2):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '11' +R
    else:
        R = '1' + R + '10'
    if int(R,2) % 7 == 0:
        R = R + bin(7)[2:]
    else:
        R = R + '1'
    if N >= 123456789 and N <= 456789012:
        print(N, R, int(R, 2))
        break


