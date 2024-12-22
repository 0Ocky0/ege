cntr = 0
for i in range(1000, 10000):
    s = str(i)
    if int(s[0]) % 2 != 0 and int(s[1]) % 2 != 0 and int(s[2]) % 2 != 0 and int(s[3]) % 2 != 0:
        k1 = int(s[0]) + int(s[1])
        k2 = int(s[2]) + int(s[3])
        first = str(min(k1, k2))
        second = str(max(k1, k2))
        s1 = first + second
        if s1 == '616':
            cntr += 1
print(cntr)
