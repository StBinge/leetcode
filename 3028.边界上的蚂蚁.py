#
# @lc app=leetcode.cn id=3028 lang=python3
#
# [3028] 边界上的蚂蚁
#
from sbw import *
# @lc code=start
class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        return sum(s==0 for s in accumulate(nums))
# @lc code=end
assert Solution().returnToBoundaryCount([3,2,-3,-4])==0
assert Solution().returnToBoundaryCount([2,3,-5])==1
