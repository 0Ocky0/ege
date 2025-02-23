mn=0
m=0
for i in range(568023,569231):
    n=2
    for j in range(2,i//2+1):
        if i%j==0:
            n+=1
    if n>m:
        m=n
        mn=i
print(m,mn)