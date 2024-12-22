def game(s, step):
    if s >= 64 and (step == 2 or step == 4):
        return True
    if s < 64 and step == 3:
        return False
    if s >= 64:
        return False

    if step % 2 == 0:
        return game(s + 1, step + 1) and game(s * 3, step + 1) and game(s + 2, step + 1)
    else:
        return game(s + 1, step + 1) or game(s * 3, step + 1) or game(s + 2, step + 1)


for s in range(1, 64):
    if game(s, 0):
        print(s)
