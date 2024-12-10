from string import *
alf = printable
for x in alf[:12]:
    for y in alf[:12]:
        otv =  int(f'{x}231{y}',12) + int(f'78{x}98{y}',14)
        if otv % 99 == 0:
            print(otv//99)