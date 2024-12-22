a = 9**8 + 3**5 - 2
s = ''
while a != 0:
    s += str(a % 3)
    a //= 3
s = s[::-1]
print(s.count("2"))