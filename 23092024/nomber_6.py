for x in range(100, 1000):
    s1 = x // 100 + x // 10 % 10
    s2 = x // 10 % 10 + x % 10
    if s1 < s2:
        otv = int(str(s1) + str(s2))
    else:
        otv = int(str(s2) + str(s1))
    if otv > 714:
        print(x, otv)