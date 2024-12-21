def game(s, step):
    if s >= 96 and step == 2:
        return True
    if s < 96 and step == 2:
        return False
    if s >= 96:
        return False

    if step % 2 == 0:
        return game(s+1,step+1) and game