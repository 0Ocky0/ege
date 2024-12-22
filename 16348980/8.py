from itertools import *
cntr = 0
for a in permutations('ПАРАБОЛА', 8):
    if 'АА' not in a and 'ОА' not in a and 'АО' not in a:
