for n in range(100, 1, -1):
    bob = bin(n)[2:]
    bob = str(bob)
    bob += str(bob.count("1") % 2)
    bob += str(bob.count("1") % 2)
    r = int(bob, 2)
    if r < 100:
        print(r)
        break