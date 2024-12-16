def game(s1, s2, step):
    if s1 + s2 >= 46 and step == 2:
        return True
    if s1 + s2 < 46 and step == 2:
        return False
    if s1 + s2 >= 46:
        return False

    if step % 2 == 0:
        return game(s1 + 1, s2 step + 1) and game(s1 + 1, s2, step + 1)game(s1 + 1, s2 step + 1) and game(s1 * 2, s2, step + 1)
    else:
        return game(s + 1, step + 1) or game(s * 2, step + 1)

