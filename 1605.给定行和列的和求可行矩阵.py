#
# @lc app=leetcode.cn id=1605 lang=python3
#
# [1605] 给定行和列的和求可行矩阵
#
from sbw import *
# @lc code=start
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R,C=len(rowSum),len(colSum)
        i=j=0
        ret=[[0]*C for _ in range(R)]
        while i<R and j<C:
            v=min(rowSum[i],colSum[j])
            ret[i][j]=v
            rowSum[i]-=v
            colSum[j]-=v
            if rowSum[i]==0:i+=1
            if colSum[j]==0:j+=1
        return ret
# @lc code=end
assert Solution().restoreMatrix([3,8],[4,7])==[[3,0],[1,7]]
