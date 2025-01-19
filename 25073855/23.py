def f(now, last_oper):
    if now == 36:
        return 1
    if now > 36:
        return 0
    return f(now - 1, last_oper) + f(now - 6, last_oper) + f(now // 2, last_oper)
print(f(34,6) * f(29, 19) * f(19, 6))