#
# @lc app=leetcode.cn id=3040 lang=python3
#
# [3040] 相同分数的最大操作数目 II
#
from sbw import *
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        L=len(nums)
        q=[]

# @lc code=end
assert Solution().maxOperations([3,2,6,1,4])==2
assert Solution().maxOperations([3,2,1,2,3,4])==3
