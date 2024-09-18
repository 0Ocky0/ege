a = 9**8 + 3**5 - 2
s = ''
while a > 0:
    s = str(a % 3) + s
    a = a // 3
print(s.count('2'))