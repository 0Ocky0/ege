a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:7]:
    for y in a[:7]:
        otv = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if otv % 181 == 0:
            print(otv // 181)