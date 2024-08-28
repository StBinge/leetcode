#
# @lc app=leetcode.cn id=1547 lang=python3
#
# [1547] 切棍子的最小成本
#
from sbw import *


# @lc code=start
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        N=len(cuts)
        f=[[0]*(N) for i in range(N)]
        for i in range(N-1,-1,-1):
            for j in range(i+2,N):
                f[i][j]=float('inf')
                cost=cuts[j]-cuts[i]
                for k in range(i+1,j):
                    f[i][j]=min(f[i][j],f[i][k]+f[k][j])
                f[i][j]+=cost
        ret=f[0][N-1]

        return ret

# @lc code=end

assert Solution().minCost(n = 9, cuts = [5,6,1,4,2]) == 22
assert Solution().minCost(7, [1, 3, 4, 5]) == 16
