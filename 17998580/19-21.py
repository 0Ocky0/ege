def game(s1, s2, step):
    if s1 + s2 >= 77 and (step == 2 or step == 4):
        return True
    if s1 + s2 < 77 and step == 4:
        return False
    if s1 + s2 >= 77:
        return False

    if step % 2 == 0:
        return game(s1 + 1, s2, step + 1) and game(s1 * 2, s2, step + 1) and game(s1, s2 + 1, step + 1) and game(s1, s2 * 2, step + 1)
    else:
        return game(s1 + 1, s2, step + 1) or game(s1 * 2, s2, step + 1) or game(s1, s2 + 1, step + 1) or game(s1, s2 * 2, step + 1)

for s2 in range(1, 69):
    if game(7, s2, 0):
        print(s2)
        break
