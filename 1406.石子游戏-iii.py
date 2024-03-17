#
# @lc app=leetcode.cn id=1406 lang=python3
#
# [1406] 石子游戏 III
#
from sbw import *
# @lc code=start
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        L=len(stoneValue)
        f=[float('-inf')]*(L+1)
        f[-1]=0
        for i in range(L-1,-1,-1):
            pre=0
            for j in range(i,min(i+3,L)):
                pre+=stoneValue[j]
                f[i]=max(f[i],pre-f[j+1])
        if f[0]==0:
            return 'Tie'
        elif f[0]>0:
            return 'Alice'
        return 'Bob'
# @lc code=end
assert Solution().stoneGameIII([1,2,3,6])=='Tie'
assert Solution().stoneGameIII([1,2,3,-9])=='Alice'
assert Solution().stoneGameIII([1,2,3,7])=='Bob'
