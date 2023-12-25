#
# @lc app=leetcode.cn id=1014 lang=python3
#
# [1014] 最佳观光组合
#
from sbw import *
# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ret=0
        L=len(values)
        mx=values[0]
        for i in range(1,L):
            ret=max(ret,values[i]-i+mx)
            mx=max(mx,values[i]+i)
        return ret
# @lc code=end
values = [8,1,5,2,6]
assert Solution().maxScoreSightseeingPair(values)==11
