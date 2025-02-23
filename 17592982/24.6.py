f = open('24_59849 (1).txt')
s = f.readline()
alfavit = '0123456789ABCDEFGHIJKLMNOP'
maxim = 0
cntr = 0
for i in range(len(s)):
    if s[i] in alfavit:
        cntr += 1
        if cntr > maxim:
            mx = cntr
    else:
        cnt = 0
mx = max(cntr, maxim)
print(mx)