#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
from typing import List
# @lc code=start
from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s=sum(nums)
        neg=s-target
        if neg<0 or neg%2:
            return 0
        neg//=2
        dp=[0]*(neg+1)
        dp[0]=1
        for n in nums:
            for j in range(neg,-1,-1):
                if j>=n:
                    dp[j]+=dp[j-n]
        return dp[-1]
# @lc code=end
assert Solution().findTargetSumWays([1,0],1)==2
assert Solution().findTargetSumWays([2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53],1000)==0
assert Solution().findTargetSumWays([1]*5,3)==5
assert Solution().findTargetSumWays([1],1)==1
