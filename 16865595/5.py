otv = []
for N in range (456789012, 456000000 + 1, -1):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '11' +R
    else:
        R = '1' + R + '10'
    r = int(R, 2)
    otv.append(r)
print(max(otv))
