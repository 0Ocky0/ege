for i in range(210235, 210300 + 1):
    deli = 0
    bob = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            deli += 1
            bob.append(j)
        if deli > 4:
            break
    if deli == 4:
        print(bob)