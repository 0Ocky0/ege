# ans = 0
# for i in range(3147, 10**10, 3147):
#     s = str(i)
#     if(s[0] == '1' and s[-1] == '1' and s[-3] == '2' and s[-4] == '0' and s[-5] == '3' and s[-6] == '4'):
#        print(s)
# print(ans)

from fnmatch import *
for i in range(3147, 10**10, 3147):
    if fnmatch(str(i), '1*4302?1'):
        print(i)