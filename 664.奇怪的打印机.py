#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        L=len(s)
        dp=[[L]*L for _ in range(L)]
        for i in range(L-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,L):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j]
                else:

                    for k in range(i,j):
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j])
        return dp[0][-1]
# @lc code=end
assert Solution().strangePrinter('aaabbb')==2
assert Solution().strangePrinter('aba')==2
