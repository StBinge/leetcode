#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
from sbw import *
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if nums[i]<nums[i+1]+nums[i+2]:
                return sum(nums[i:i+3])
        return 0

# @lc code=end
nums = [1,2,1,10]
assert Solution().largestPerimeter(nums)==0
nums = [2,1,2]
assert Solution().largestPerimeter(nums)==5
