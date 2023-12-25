#
# @lc app=leetcode.cn id=1000 lang=python3
#
# [1000] 合并石头的最低成本
#
from sbw import *
# @lc code=start
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        L=len(stones)
        if (L-1)%(k-1):
            return -1
        
        presums=list(accumulate(stones,initial=0))

        f=[[0]*L for _ in range(L)]
        for i in range(L-1,-1,-1):
            for j in range(i+1,L):
                f[i][j]=min(f[i][m]+f[m+1][j] for m in range(i,j,k-1))
                if (j-i) % (k-1)==0:
                    f[i][j]+=presums[j+1]-presums[i]
        return f[0][-1]
        
# @lc code=end
stones = [3,2,4,1]
K = 2
assert Solution().mergeStones(stones,2)==20