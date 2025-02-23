a = open('demo_2025_24.txt').read()
a = a.replace('-', '*')
a = a.replace('*0*', '*5*')
while '**' in a:
    a = a.replace('**', '*x*')
a = a.replace('*0', 'x')
a = a.replace('x0', 'x')
a = a.split('x')
ml = 0
for i in a:
    if len(i) > 1:
        if i[0] == '*':
            i = i[1:]
        if i[-1] == '*':
            i = i[:-1]
        ml = max(ml, len(i))
print(ml)
