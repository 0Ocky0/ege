def f(x,y,z,w):
    return (((y or z) <= (z and w)) == (not((x and z) <= (w or y))))
print('x,y,z,w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if f(x,y,z,w) == 1:
                    print(x,y,z,w)