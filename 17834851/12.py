s = '21' * 10 + '2' * 100
cntr = 0
while '21' in s:
    s = s.replace('21', '5', 1)
    cntr += 1
    if cntr * 5 + s.count('1') == 34:
        print(cntr)
