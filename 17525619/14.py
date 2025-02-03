a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:15]:
    for y in a[:15]:
        otv = int(f'90{x}4{y}', 15) + int(f'91{x}{y}2', 16)
        if otv % 56 == 0:
            print(otv // 56)