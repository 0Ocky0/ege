s = open('24 (4).txt').readline()
max_cnt = 0
cnt = 0

for i in range(len(s)):
    if s[i] == 'A' or :
        cnt+=1
    else:
        cnt=0
    max_cnt = max(max_cnt, cnt)

print(max_cnt)