a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:22]:
        otv = int(f'63{x}59685', 22) + int(f'17{x}53', 22) + int(f'36{x}5', 22)
        if otv % 21 == 0:
            print(otv // 21)