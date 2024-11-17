from string import *
alf = digits
for x in alf[:9]:
    for y in alf[:9]:
        otv = int(f'88{x}4{y}', 9) + int(f'7{x}44{y}', 11)
        if otv % 61 == 0:
            print(otv // 61)
