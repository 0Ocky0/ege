def f(now, last_oper):
    if now == 20:
        return 1
    if now > 20:
        return 0
    else:
        return f(now + 2, last_oper) + f(now + 5, last_oper)
print(f(1,20))