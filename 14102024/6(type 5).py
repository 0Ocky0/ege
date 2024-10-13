for i in range(3, 3000):
    x = bin(i)[2:]
    x = x[:-1]
    if i % 2 == 0:
        x = x + '10'
    else:
        x = x + '01'
    otv = int(x, 2)
    if otv == 2018:
        print(i, otv)