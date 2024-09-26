from itertools import product
k = 0
for i in product("АКРУ",repeat=5):
        k += 1
        if k==450:
            print(''.join(i))