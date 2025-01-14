from itertools import *

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cntr = 0
for nums in product(nums[:15], repeat=8):
    if nums.count('0') == 2 and (nums[0] != '0' and nums[1] != '0') and nums.count('A') + nums.count('B') + nums.count(
            'C') + nums.count('D') + nums.count(
            "E") + nums.count('F') <= 4:
        print(nums)
        cntr += 1
print(cntr)
