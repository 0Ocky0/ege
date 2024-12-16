f = open('69927.txt').readlines()
nums = [int(lines) for lines in f]
otv = []
otvetik = []
for i in nums:
    if i % 32 == 0:
        otv.append(i)
for a, b in zip(nums, nums[1:]):
    if (a < 0 or b < 0) and ((a + b) < len(otv)):
        otvetik.append(a + b)
print(len(otvetik), max(otvetik))
