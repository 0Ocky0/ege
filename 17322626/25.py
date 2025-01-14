from fnmatch import *
for n in range(0, 10**10, 2024):
    if fnmatch(str(n), '3?2258*4'):
        print(n)