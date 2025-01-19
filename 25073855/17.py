f = open('17_19249 (1).txt').readlines()
nums = [int(l) for l in f]
otv = []
maxim = -10**8
for i in nums:
    if len(str(abs(i))) == 5 and abs(i) % 100 == 43:
        maxim = max(i, maxim)
for a1, a2, a3 in zip(nums, nums[1:], nums[2:]):
    if (len(str(abs(a1))) == 5 and abs(a1) % 100 == 43) or (len(str(abs(a2))) == 5 and abs(a2) % 100 == 43) or (
            len(str(abs(a3))) == 5 and abs(a3) % 100 == 43):
        if a1 ** 2 + a2 ** 2 + a3 ** 2 <= maxim**2:
            otv.append(a1 ** 2 + a2 ** 2 + a3 ** 2)
print(len(otv), min(otv))