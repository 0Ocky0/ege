from string import *
alf = digits
for x in alf[:7]:
    for y in alf[:7]:
        otv = int(f'{y}{x}320', 7) + int(f'1{x}3{y}3', 9)
        if otv % 181 == 0:
            print(otv // 181)
