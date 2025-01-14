f = open('17.txt').readlines()
nums = [abs(int(i)) for i in f]
otv = []
maxim = -999999999
for i in nums:
    if i % 10 == 3:
        maxim = max(maxim, i)
for a, b in zip(nums, nums[1:]):
    if int(a % 10 == 3) + int(b % 10 == 3) == 1 and a ** 2 + b**2 >= maxim**2:
        otv.append(a**2 + b ** 2)
print(len(otv), max(otv))