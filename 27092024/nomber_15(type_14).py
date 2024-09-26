otv = 125 + 25**3 + 5**9
real = ''
while otv > 0:
    real += str(otv  % 5)
    otv = otv//5
real = real[::-1]
print(real.count('0'), real)