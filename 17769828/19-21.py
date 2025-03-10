def game(x, k, v):
    if x <= 17:
        return k in v
    if k >= max(v):
        return 0
    h = [game(x - 1, k + 1, v)]
    if x % 3 == 0:
        h.append(game(x // 3, k + 1, v))
    else:
        h.append(game(x - 2, k + 1, v))
    if x % 5 == 0:
        h.append(game(x // 5, k + 1, v))
    else:
        h.append(game(x - 3, k + 1, v))
    if k % 2 != max(v) % 2:
        return any(h)
    else:
        return all(h)

for x in range(17, 10000):
    if game(x, 0, [2, 4]) == 1 and game(x, 0, [2]) == 0:
        print(x)
        break