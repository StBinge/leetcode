#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#
from sbw import *


# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ret = 0
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                s += nums[i]
            else:
                ret = max(s, ret)
                s = nums[i]
        return max(ret, s)


# @lc code=end
assert Solution().maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33
assert Solution().maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65
