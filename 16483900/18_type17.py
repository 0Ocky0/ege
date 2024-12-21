f = open('17 (17).txt').readlines()
nums = [int(lines) for lines in f]
otv = []
for a, b in zip(nums, nums[1:]):
    if (a * b) % 10 == 0:
        otv.append(a+b)
print(len(otv), max(otv))