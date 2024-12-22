def game(s, step):
    if s >= 32 and step == 3:
        return True
    if s < 32 and step == 3:
        return False
    if s >= 32:
        return False
    if step % 2 == 0:
        return game(s + 1, step + 1) or game(s * 3 + 1, step + 1)
    else:
        return game(s + 1, step + 1) and game(s * 3 + 1, step + 1)

for s in range(1, 32):
    if game(s, 0):
        print(s)