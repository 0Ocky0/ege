def f(x,y,z,w):
    return ( (y <= z) and not((y or w) <= (z and x)) )
print('z,w,x,y')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x,y,z,w) == 1:
                    print(z,w,x,y)