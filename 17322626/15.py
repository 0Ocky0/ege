cntr = 0
for A in range(500):
    Flag = True
    for x in range(500):
        for y in range(500):
            if not(((x < 6) <= (x**2 < A)) and ((y**2 <= A) <= (y <= 6))):
                Flag = False
                break
    if Flag:
        cntr += 1
print(cntr)