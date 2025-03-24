s = open('24 (7).txt').readline()
max_len = 0
cnt = 2
for i in range(len(s)-2):
    if (s[i] == 'A' or s[i] == 'B') and (s[i + 1] == 'A' or s[i + 1] == 'B') and (s[i + 2] == 'A' or s[i + 2] == 'B'):
        cnt = 2
    else:
        cnt += 1
    max_len = max(max_len, cnt)
print(max_len)

