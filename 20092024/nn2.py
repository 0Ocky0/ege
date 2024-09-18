def f(x,y,z,w):
    return (((x or (not(y))) or ((not(z))==w)) <= (y and z))
print('x,y,z,w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x,y,z,w) == 0:
                    print(x,y,z,w)