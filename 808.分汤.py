#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] 分汤
#

# @lc code=start
# from functools import cache
class Solution:
    def soupServings(self, n: int) -> float:
        cache={}
        n=(n+24)//25
        if n>=179:
            return 1.0
        # d[a][b]
        d=[[0]*(n+1) for _ in range(n+1)]
        d[0][0]=0.5
        for i in range(1,n+1):
            d[0][i]=1
        for i in range(1,n+1):
            for j in range(1,n+1):
                p=d[max(0,i-4)][j]+d[max(0,i-3)][max(0,j-1)]+d[max(0,i-2)][max(0,j-2)]+d[max(0,i-1)][max(0,j-3)]
                d[i][j]=p/4
        return d[n][n]
# @lc code=end
# assert Solution().soupServings(25)==1
assert abs(Solution().soupServings(800)-0.96162)<10**-5
assert Solution().soupServings(50)==0.625
assert Solution().soupServings(100)==0.71875
