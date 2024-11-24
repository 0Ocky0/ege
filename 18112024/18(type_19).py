def game(s1, s2, step):
    if s1 >= 48 or s2 >= 48 and step == 2:
        return True
    if s1 < 48 or s2 < 48 and step == 2:
        return False

    if step % 2 == 0:
        return game(s1 + 1, s2, step + 1) or game(s1 * 2, s2, step + 1) or game(s1, s2 + 2, step + 1) or game(s1, s2 * 2, step + 1)
    else:
        return game(s1 + 2, s2, step + 1) or game(s1 * 2, s2, step + 1) or game(s1, s2 + 2, step + 1) or game(s1, s2 * 2, step + 1)

for s2 in range(1, 114):
    if game(3, s2, 0):
        print(s2)
        break
