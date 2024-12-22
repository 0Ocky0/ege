from itertools import *
cntr = 0
for n in product('012345678', repeat = 5):
    bob = ''.join(n)
    if bob[0] != '0' and bob.count('3') == 2:
        for x in bob:
            if x in '1357': bob = bob.replace(x, '*')
        if '2*' not in bob and '*2' not in bob:
            cntr += 1
print(cntr)