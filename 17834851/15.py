for a in range(1, 1000):
    cntr = 0
    for x in range(1, 501):
        if (120 % a == 0) and ((not(x % a == 0)) <= ((x % 18 == 0) <= (not(x % 24 == 0)))):
            cntr+= 1
    if cntr == 500:
        print(a)