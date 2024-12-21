from functools import lru_cache
@lru_cache()
def f(now):
    if now == 32:
        return 1
    if now > 32:
        return 0
    return f(now + 1) + f(now + 10)
print(f(10))