from itertools import *
cntr = 0
for a in product('01234567', repeat = 5):
    if a[0] != '0' and '1' not in a and len(a) == len(set(a)):
        bob = 0
        for i in range(1, len(a)):
            if int(int(a[i]) % 2 == 0) == int(int(a[i - 1]) % 2 == 0):
                bob += 1
        if bob == 0:
            cntr += 1
            print(a)
print(cntr)