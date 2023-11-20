#
# @lc app=leetcode.cn id=526 lang=python3
#
# [526] 优美的排列
#

# @lc code=start
class Solution:
    def countArrangement(self, n: int) -> int:
        dp=[0]*(1<<n)
        dp[0]=1
        for mask in range(1,(1<<n)):
            num=bin(mask).count('1')
            for i in range(n):
                if mask & (1<<i) and (num%(i+1)==0 or (i+1)%num==0):
                    dp[mask]+=dp[mask ^ (1<<i)]
        return dp[-1]
# @lc code=end
assert Solution().countArrangement(2)==2
assert Solution().countArrangement(1)==1
assert Solution().countArrangement(3)==3
assert Solution().countArrangement(7)==41
