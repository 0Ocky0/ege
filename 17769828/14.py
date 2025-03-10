a = 36 ** 7 + 6 ** 19 - 18
bob = ''
while a > 0:
    bob = str(a % 6) + bob
    a = a // 6
print(bob.count('0'), bob)