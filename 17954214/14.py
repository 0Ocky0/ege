a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for x in a[:15]:
    if (int(f'123{x}5', 15) + int(f'1{x}233', 15)) // 14:
        print((int(f'123{x}5', 15) + int(f'1{x}233', 15)) // 14)