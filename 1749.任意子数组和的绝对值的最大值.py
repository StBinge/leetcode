#
# @lc app=leetcode.cn id=1749 lang=python3
#
# [1749] 任意子数组和的绝对值的最大值
#
from sbw import *


# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)


# @lc code=end
assert (
    Solution().maxAbsoluteSum(
        [-3, -5, -3, -2, -6, 3, 10, -10, -8, -3, 0, 10, 3, -5, 8, 7, -9, -9, 5, -8]
    )
    == 27
)
assert Solution().maxAbsoluteSum([2, -5, 1, -4, 3, -2]) == 8
assert Solution().maxAbsoluteSum([1, -3, 2, 3, -4]) == 5
