from string import *
alf = printable
for x in alf[:8]:
    for y in alf[:8]:
        otv =  int(f'{x}01{y}4',9) + int(f'{x}{y}544',8)
        if otv % 89 == 0:
            print(otv//89)