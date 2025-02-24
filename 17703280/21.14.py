a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in a[:9]:
    for y in a[:9]:
        otv = int(f'2{y}66{x}', 9) + int(f'{x}0{y}1', 12)
        if otv % 170 == 0:
            print(otv // 170)