def game(s, step):
    if s >= 132 and (step == 2 or step == 4):
        return True
    if s < 132 and step == 4:
        return False
    if s >= 132:
        return False

    if step % 2 == 0:
        return game(s + 3, step + 1) and game(s + 6, step + 1) and game(s * 3, step + 1)
    else:
        return game(s + 3, step + 1) or game(s + 6, step + 1) or game(s * 3, step + 1)


for s in range(1, 131):
    if game(s, 0):
        print(s)
