def game(s, step):
    if s >= 129 and (step == 2 or step == 4):
        return True
    if s < 129 and step == 4:
        return False
    if s >= 129:
        return False

    if step % 2 == 0:
        return game(s + 1, step + 1) and game(s * 2, step + 1)
    else:
        return game(s + 1, step + 1) or game(s * 2, step + 1)


for s in range(1, 128):
    if game(s, 0):
        print(s)
