a = 25**5+5**13-5
otv = ''
while a > 0:
    otv = str(a % 5) + otv
    a = a//5
print(otv.count('4'))