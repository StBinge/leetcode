#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start

class Solution:
    def fib(self, n: int) -> int:
        if n<1:
            return 0 
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
# @lc code=end
assert Solution().fib(0)==0
assert Solution().fib(1)==1
assert Solution().fib(2)==1
assert Solution().fib(3)==2
assert Solution().fib(4)==3
