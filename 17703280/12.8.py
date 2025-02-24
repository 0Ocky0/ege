from itertools import *

cntr = 0
for a in permutations('ЯРОСЛАВ', r= 5):
    bob = ''.join(a)
    bob = bob.replace('Я', 'A').replace('О', 'A').replace('А', 'A')
    bob = bob.replace('Р', 'B').replace('С', 'B').replace('Л', 'B').replace('В', 'B')
    if bob.count('B') > bob.count('A') and 'AA' not in bob:
        cntr += 1
print(cntr)
