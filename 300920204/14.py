from string import *

alf = printable
for x in alf[:11]:
    for y in alf[:11]:
        otv = int(f'{x}341{y}', 11) + int(f'56{x}1{y}', 19)
        if otv % 305 == 0:
            print(otv // 305)
