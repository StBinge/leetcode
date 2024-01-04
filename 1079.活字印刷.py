#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#
from sbw import *
# @lc code=start
from math import comb
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        values=Counter(tiles).values()
        L=len(tiles)
        N=len(values)
        # f=[[0]*(L+1) for _ in range(N+1)]
        # f[0][0]=1
        f=[0]*(L+1)
        f[0]=1
        n=0
        for cnt in values:
            n+=cnt
            for j in range(n,0,-1):
                for k in range(1,min(j,cnt)+1):
                    f[j]+=f[j-k]*comb(j,k)
        return sum(f[1:])
# @lc code=end
assert Solution().numTilePossibilities('AAB')==8
