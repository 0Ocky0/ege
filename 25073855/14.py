a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:25]:
    otv = int(f'11353{x}12', 25) + int(f'135{x}21', 25)
    if otv % 24 == 0:
        print(otv // 24, x)
