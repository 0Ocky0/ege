a = '012345678'
for x in a:
    m = int(f'842{x}5', 9)
    n = int(f'8{x}725', 9)
    for A in range(1, 10000):
        if (m + A) % n == 0:
            print(A, x)