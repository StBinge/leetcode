#
# @lc app=leetcode.cn id=1752 lang=python3
#
# [1752] 检查数组是否经排序和轮转得到
#
from sbw import *


# @lc code=start
class Solution:
    def check(self, nums: List[int]) -> bool:

        N = len(nums)

        for i in range(1, N):
            if nums[i] < nums[i - 1]:
                for j in range(i + 1, N):
                    if nums[j] < nums[j - 1]:
                        return False
                else:
                    return nums[0]>=nums[-1]
        return True


# @lc code=end
assert Solution().check([1, 2, 3])
assert Solution().check([2, 1, 3, 4]) == False
assert Solution().check([3, 4, 5, 1, 2])
