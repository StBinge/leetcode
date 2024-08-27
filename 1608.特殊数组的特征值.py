#
# @lc app=leetcode.cn id=1608 lang=python3
#
# [1608] 特殊数组的特征值
#
from sbw import *


# @lc code=start
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        for i in range(1, n + 1):
            if nums[i - 1] >= i and (i == n or nums[i] < i):
                return i
        return -1


# @lc code=end
assert Solution().specialArray([3, 6, 7, 7, 0]) == -1
assert Solution().specialArray([0, 0]) == -1
assert Solution().specialArray([3, 5]) == 2
assert Solution().specialArray([0, 4, 3, 0, 4]) == 3
