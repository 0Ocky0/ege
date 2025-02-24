import sys

sys.setrecursionlimit(10**8)
def f(n):
    if n == 1:
        return n
    if n > 1:
        return n - 1 + f(n - 1)
print(f(2024) - f(2022))