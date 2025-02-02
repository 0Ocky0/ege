def f(now, last_oper):
    if now == 16:
        return 1
    if now > 16 or now == 6 or now == 12:
        return 0
    else:
        return f(now + 1, last_oper) + f(now * 2, last_oper) + f(now + 3, last_oper)
print(f(3,16))