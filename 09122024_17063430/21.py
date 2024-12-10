def game(s1, s2, step):
    if s1 + s2 >= 59 and step == 3:
        return True
    if s1 + s2 < 59 and step == 3:
        return False
    if s1 + s2 >= 59:
        return False

    if step % 2 != 0:
        return game(s1 + 1, s2, step + 1) and game(s1 * 2, s2, step + 1) and game(s1, s2 + 1, step + 1) and game(s1, s2 * 2, step + 1)
    else:
        return game(s1 + 1, s2, step + 1) or game(s1 * 2, s2, step + 1) or game(s1, s2 + 1, step + 1) or game(s1, s2 * 2, step + 1)

for s2 in range(1, 53):
    if game(5, s2, 0):
        print(s2)