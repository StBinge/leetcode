#
# @lc app=leetcode.cn id=1877 lang=python3
#
# [1877] 数组中最大数对和的最小值
#
from sbw import *


# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-1 - i] for i in range(len(nums) // 2))


# @lc code=end
assert Solution().minPairSum([3, 5, 4, 2, 4, 6]) == 8
assert Solution().minPairSum([3, 5, 2, 3]) == 7
