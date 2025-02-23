def f(now, s):
    if now == 16:
        s += 1
    if now == 2 and s == 1:
        return 1
    if now < 2:
        return 0
    return f(now - 2, s) + f(now // 2, s)
print(f(38, 0))
