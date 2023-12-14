#
# @lc app=leetcode.cn id=961 lang=python3
#
# [961] 在长度 2N 的数组中找出重复 N 次的元素
#
from sbw import *


# @lc code=start
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        l=len(nums)
        for g in range(1,4):
            for i in range(l):
                if i+g>=l:
                    break
                if nums[i]==nums[i+g]:
                    return nums[i]


# @lc code=end
nums=[2,6,2,1]
assert Solution().repeatedNTimes(nums) == 2

nums = [2, 1, 2, 5, 3, 2]
assert Solution().repeatedNTimes(nums) == 2

nums = [1, 2, 3, 3]
assert Solution().repeatedNTimes(nums) == 3
