f = open('24 (8).txt').readline()
max_len = 0
cnt = 2
for i in range(len(s)-2):
    if s[i] == '0' and s[i + 1] == '0' and s[i + 2] == '0':
        cnt = 2
    else:
        cnt += 1
    max_len = max(max_len, cnt)
print(max_len)
