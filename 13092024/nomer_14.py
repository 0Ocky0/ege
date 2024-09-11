from string import * #чтобы точно не ошибиться, я просто забыл, там А это 10 или 11
alf = digits+ascii_uppercase
for x in alf[:13]:
    otv =  int(f'26{x}98',13) + int(f'4{x}296',13)
    if otv % 34 == 0:
        print(otv//34)