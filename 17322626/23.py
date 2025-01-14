def f(now, last_oper):
    if now == 24:
        return 1
    if now < 24:
        return 0
    return f(now + 1, last_oper) + f(now * 2, last_oper)


print(f(2, 12) * f(12, 24) * f(2, 11) * f(11, 24))
