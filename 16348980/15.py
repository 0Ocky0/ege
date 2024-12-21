minim = 99999999
otv = []
for l in range(-100, 100):
    for r in range(l, 100):
        f = True
        for x in range(-100, 100):
            inp = x >= 17 and x <= 54
            inq = x >= 37 and x <= 83
            ina = x >= l and x <= r
            exp = (inp) <= (((inq) and (not (ina))) <= (not (inp)))
            if not exp:
                f = False
                break
        if f:
            minim = min(minim, abs(r - l))
print(minim)