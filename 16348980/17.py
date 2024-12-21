f = open('17 (18).txt').readlines()
otv = []
nums = [int(lines) for lines in f]
for a, b in zip(nums, nums[1:]):
    if (a + b) % 120 == 0:
        otv.append(a+b)
print(len(otv), max(otv))