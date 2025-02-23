from fnmatch import *
for num in range(0, 10**8, 2622):
    if fnmatch(str(num), '1?4*6?8'):
        print(num, num // 2622)