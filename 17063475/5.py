for i in range(1000,10000):
    a = str(i)
    first = int(a[0]) + int(a[1])
    sec = int(a[1]) + int(a[2])
    third = int(a[2]) + int(a[3])
    vce = [str(first), str(sec), str(third)]
    vce.sort()
    vce.pop(0)
    otv = vce[0] + vce[1]
    if otv == '1215':
        print(i)