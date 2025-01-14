strok = '123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for x in strok[:11]:
    for y in strok[:11]:
        otv = int(f'{y}AA{x}', 12) + int(f'{x}02{y}', 14)
        if otv % 80 == 0:
            print(otv // 80)