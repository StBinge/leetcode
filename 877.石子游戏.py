#
# @lc app=leetcode.cn id=877 lang=python3
#
# [877] 石子游戏
#
from typing import List
# @lc code=start
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        f=[0]*n
        for i in range(n):
            f[i]=piles[i]
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                f[j]=max(piles[i]-f[j],piles[j]-f[j-1])
        return f[-1]>0
# @lc code=end

