#
# @lc app=leetcode.cn id=3068 lang=python3
#
# [3068] 最大节点价值之和
#
from sbw import *
# @lc code=start
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        f0,f1=0,float('-inf')
        for n in nums:
            f0,f1=max(f0+n,f1+(n^k)),max(f1+n,f0+(n^k))
        return f0
# @lc code=end
assert Solution().maximumValueSum(nums = [1,2,1], k = 3, edges = [[0,1],[0,2]])==6
