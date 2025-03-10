from fnmatch import *
for num in range(0, 10 ** 10 + 1, 3147):
    if fnmatch(str(num), '1*4239?7'):
        print(num, num // 3147)