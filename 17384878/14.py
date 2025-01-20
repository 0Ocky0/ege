a = 125 ** 5 + 25 ** 9 - 30
bob = ''
while a > 0:
    bob = str(a % 5) + bob
    a = a // 5
print(bob.count('4'))