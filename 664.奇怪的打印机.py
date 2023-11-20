#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] 奇怪的打印机
#

# @lc code=start
class Solution:
    def strangePrinter(self, s: str) -> int:
        L=len(s)
        dp=[[100]*L for _ in range(L)]
        # for i in range(L):
        for i in range(L-1,-1,-1):
            dp[i][i]=1
            for j in range(i+1,L):
                if s[i]==s[j]:
                    dp[i][j]=min(dp[i][j],dp[i][j-1])
                else:
                    cnt=100
                    for k in range(i,j):
                        cnt=min(cnt,dp[i][k]+dp[k+1][j])
                    dp[i][j]=cnt

        return dp[0][-1]

# @lc code=end
assert Solution().strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa")==19
assert Solution().strangePrinter('aba')==2
assert Solution().strangePrinter('aaabbb')==2
