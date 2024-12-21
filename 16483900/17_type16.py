def F(n):
    if n == 1:
        return 1
    if n % 2 != 0 and n > 1:
        return n+F(n-2)
    if n % 2 == 0:
        return n*F(n-1)
print(F(40))