f = open('17 (16).txt').readlines()
nums = [int(lines) for lines in f]
maxim = max([x for x in nums if int(x) % 1000 == 123])
otv = []
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if (int(len(str(a)) == 5) + int(len(str(b)) == 5) + int(len(str(c)) == 5) >= 2) and (int(a% 3 == 0) + int(b % 3 == 0) + int(c % 3 == 0) == 1) and (a + b + c > int(maxim)):
        otv.append(a + b + c)
print(len(otv), max(otv))