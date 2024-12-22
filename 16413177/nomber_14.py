from string import *
alf = printable
for x in alf[:12]:
    otv =  int(f'28{x}2',18) + int(f'93{x}5',12)
    if otv % 133 == 0:
        print(otv//133)