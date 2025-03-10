bob = '7' * 40 + '9' * 40 + '4' * 50
while '49' in bob or '97' in bob or '47' in bob:
    if '47' in bob:
        bob = bob.replace('47', '74', 1)
        print(bob)
    if '97' in bob:
        bob = bob.replace('97', '79', 1)
        print(bob)
    if '49' in bob:
        bob = bob.replace('49', '94', 1)
        print(bob)
print(bob[24], bob[70], bob[104])