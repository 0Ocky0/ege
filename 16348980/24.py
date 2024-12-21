f = open('24 (5).txt').read()
now_list = [f[0]]
maxim = 0
for i in range (1, len(f)):
    now_list.append(f[i])
    if {f[i], f[i - 1]} == {'a', 'd'}:
        now_list.clear()
        now_list.append(f[i])
    maxim = max(maxim, len(now_list))
print(maxim)