for n in range(1000, 10000):
    s = str(n)
    sum1 = int(s[0]) + int(s[1])
    sum2 = int(s[1]) + int(s[2])
    sum3 = int(s[2]) + int(s[3])
    first = str(sum1 + sum2 + sum3 - max(sum1, sum2, sum3) - min(sum1, sum2, sum3))
    second = str(max(sum1, sum2, sum3))
    s1 = first + second
    if s1 == '1315':
        print(n)