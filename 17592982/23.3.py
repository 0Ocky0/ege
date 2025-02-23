def f(x, y, k):
    if x > y + 1:
        return 0
    if x == y:
        return 1
    else:
        if k == 1:
            return f(x * 2, y, k - 1) + f(x * 3, y, k - 1)
        else:
            return f(x - 1, y, k + 1) + f(x * 2, y, k) + f(x * 3, y, k)


print(f(3, 15, 0))
