#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新 21 点
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp=[0]*(k+maxPts)
        bound=min(n,k+maxPts-1)
        for i in range(k,bound+1):
            dp[i]=1
        dp[k-1]=(bound-k+1)/maxPts
        for i in range(k-2,-1,-1):
            # dp[i]=dp[i+1]-(dp[i+1]-dp[i+1+maxPts])/maxPts
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts
        return dp[0]
# @lc code=end
assert Solution().new21Game(21,17,10)==0.73278
n = 10
k = 1
maxPts = 10
ret=1.00000
assert Solution().new21Game(n,k,maxPts)==1
assert Solution().new21Game(6,1,10)==0.6

