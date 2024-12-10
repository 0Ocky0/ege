f = open('17.txt')
otv = []
maxim = 0
nums = [int(lines) for lines in f]
for i in nums:
    if i % 100 == 17 and i > maxim:
        maxim = i
for a, b, c in zip(nums, nums[1:], nums[2:]):
    if (int(len(str(a)) == 4) + int(len(str(b)) == 4) + int(len(str(c)) == 4)) == 2 and (
            a % 5 == 0 or b % 5 == 0 or c % 5 == 0) and (a + b + c > maxim):
        otv.append(a + b + c)
print(len(otv), max(otv))
