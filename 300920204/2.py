def f(x,y,z,w):
    return ((z and y) or ((x<=z)==(y<=w)))
print('w,z,y,x')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x,y,z,w)==0:
                    print(w,z,y,x)