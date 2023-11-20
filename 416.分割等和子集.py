#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import List
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N=len(nums)
        if N<2:
            return False
        S=sum(nums)
        if S&1:
            return False
        M=max(nums)
        target=S//2
        if M>target:
            return False
        dp=[False]*(target+1)
        dp[0]=True
        dp[nums[0]]=True
        for i in range(1,N):
            for j in range(target,0,-1):
                if j>nums[i]:
                    dp[j]=dp[j] or dp[j-nums[i]]
                else:
                    dp[j]=dp[j]
        return dp[-1]
# @lc code=end

assert Solution().canPartition([1,5,11,5])
assert Solution().canPartition([1,2,3,5])==False