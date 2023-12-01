#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
from typing import List


# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc=True
        dec=True
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                dec=False
            elif nums[i]<nums[i-1]:
                inc=False
        return inc or dec



# @lc code=end
assert Solution().isMonotonic([11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]) == False
assert Solution().isMonotonic([1, 3, 2]) == False
assert Solution().isMonotonic([1, 2, 2, 3])
assert Solution().isMonotonic([6, 5, 4, 4])
