from fnmatch import *
for num in range(0, 10 ** 10 + 1, 2024):
    if fnmatch(str(num), '1?2157*4'):
        print(num, num // 2024)