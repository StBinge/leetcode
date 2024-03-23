#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#
from sbw import *
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        big=little=0
        for n in nums:
            if n>big:
                big,little=n,big
            elif n>little:
                little=n
        return (big-1)*(little-1)
# @lc code=end
assert Solution().maxProduct([3,4,5,2])==12
