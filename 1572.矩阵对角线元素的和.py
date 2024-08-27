#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#
from sbw import *
# @lc code=start
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N=len(mat)
        ret=sum(mat[i][i]+mat[i][N-i-1] for i in range(N))
        if N&1:
            ret-=mat[N//2][N//2]
        return ret
# @lc code=end
assert Solution().diagonalSum([[1,2,3],
            [4,5,6],
            [7,8,9]])==25
