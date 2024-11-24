from string import *
alf = digits
for x in alf[:8]:
    for y in alf[:8]:
        otv = int(f'{y}04{x}5', 11) + int(f'253{x}{y}', 8)
        if otv % 117 == 0:
            print(otv // 117)