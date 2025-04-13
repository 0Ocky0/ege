a = 2 * 216 ** 6 + 3 * 36 - 432
bob = ''
while a > 0:
    bob = str(a % 6) + bob
    a = a // 6
print(bob.count('5'))
