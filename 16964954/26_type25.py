from fnmatch import *
for i in range(0,10**9+1,2031):
    if fnmatch(str(i),'*31*65?') and i%31==0:
        d=[]
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                d.append(j)
                if j!=(i//j):
                    d.append(i//j)
        for x in range(100):
            if len(d)==2**x:
                print(i,i//2031)
                break