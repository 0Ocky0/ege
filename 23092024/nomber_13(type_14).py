from string import *
alf = printable
for x in alf[:19]:
    otv =  int(f'98897{x}21',19) + int(f'2{x}923',19)
    if otv % 18 == 0:
        print(otv//18)