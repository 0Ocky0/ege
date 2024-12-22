def f(x,y,z):
    return (x or y) <= (y == z)
print('z,x,y')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if f(x,y,z) == 0:
                print(z,x,y)