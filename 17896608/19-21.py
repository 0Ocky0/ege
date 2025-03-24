def game(s1, s2, step):
    if s1 + s2 >= 49 and(step == 2 or step == 4):
        return True
    if s1 + s2 < 49 and step == 4:
        return False
    if s1 + s2 >= 49:
        return False

    if step % 2 == 0:
        return game(s1 + 1, s2, step + 1) and game(s1 * 3, s2, step + 1) and game(s1, s2 + 1, step + 1) and game(s1, s2 * 3, step + 1)
    else:
        return game(s1 + 1, s2, step + 1) or game(s1 * 3, s2, step + 1) or game(s1, s2 + 1, step + 1) or game(s1, s2 * 3, step + 1)

for s2 in range(1, 43 + 1):
    if game(5, s2, 0):
        print(s2)
        break