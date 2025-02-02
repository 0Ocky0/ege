def f(n):
    if n == 0:
        return 0
    if n > 0 and n % 3 == 0:
        return n // 3
    if n % 3 > 0:
        return n % 3 + f(n - n % 3)
i = 0
while f(i) != 11:
    i += 1
print(i)