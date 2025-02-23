a = open('69932 (1).txt').readline()
a = a.replace('*-', ';')
a = a.replace('**', ';')
a = a.replace('-*', ';')
a = a.replace('--', ';')
a = a.replace('-;', ';')
a = a.replace(';-', '!')
a = a.replace(';*', ';')
a = a.replace('*;', ';')
a = a.replace('-0', ';')
a = a.replace('0-', ';')
a = a.replace('0*', ';')
a = a.replace('*0', ';')
a = a.split(';')
maxi = 0
for i in range(1, len(a)):
    s = a[i]
    cnt = 0
    flag = 0
    for j in range(1, len(s)):
        if flag == 0 and a[j] != '0':
            flag = 1
        if flag == 1:
            cnt += 1
    maxi = max(maxi, cnt)
print(maxi)
