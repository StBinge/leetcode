#
# @lc app=leetcode.cn id=1140 lang=python3
#
# [1140] 石子游戏 II
#
from sbw import *
# @lc code=start
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        L=len(piles)
        sum=0
        f=[[0]*(L+1) for _ in range(L+1)]
        for i in range(L-1,-1,-1):
            sum+=piles[i]
            for M in range(1,L+1):
                if i+2*M>=L:
                    f[i][M]=sum
                    continue
                for x in range(1,2*M+1):
                    if x+i>L:
                        break
                    f[i][M]=max(f[i][M],sum-f[i+x][max(x,M)])
        return f[0][1]
# @lc code=end
assert Solution().stoneGameII(piles = [1,2,3,4,5,100])==104
assert Solution().stoneGameII(piles = [2,7,9,4,4])==10
