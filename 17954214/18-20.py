def game(x, s):
    if x >= 63 and (s == 2 or s == 4):
        return True
    if x < 63 and s == 4:
        return False
    if x >= 63:
        return False
    if s % 2 == 0:
        return game(x + 1, s + 1) and game(x + 4, s + 1) and game(x * 5, s + 1)
    else:
        return game(x + 1, s + 1) or game(x + 4, s + 1) or game(x * 5, s + 1)


for x in range(2, 62):
    if game(x, 0):
        print(x)
