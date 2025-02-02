a = 36 ** 8 + 6 ** 20 - 12
bob = ''
while a > 0:
    bob = str(a % 6) + bob
    a = a // 6
print(bob.count('5'), bob)