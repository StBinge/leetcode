#
# @lc app=leetcode.cn id=486 lang=python3
#
# [486] 预测赢家
#
from typing import List
# @lc code=start
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N=len(nums)
        dp=nums.copy()
 
        for l in range(N-2,-1,-1):
            for r in range(l+1,N):
                dp[r]=max(nums[l]-dp[r],nums[r]-dp[r-1])
                # dp[l][r]=max(nums[l]-dp[l+1][r],nums[r]-dp[l][r-1])
        return dp[-1]>=0

# @lc code=end
assert Solution().predictTheWinner([1,5,2])==False
assert Solution().predictTheWinner([1,5,233,7])==True
