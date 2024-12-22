from itertools import product
s = product('НЧ', repeat = 11)
cnt1 = 0
cnt2 = 0
for i in s:
    p=''.join(i)
    if p.count('НН') == 0 and p.count('Н') == 3:
        if p[0] == 'Н':
            cnt1 += 1
        else:
            cnt2 += 1
print(4**11*cnt1 + 3*4**10*cnt2)