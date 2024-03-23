#
# @lc app=leetcode.cn id=1314 lang=python3
#
# [1314] 矩阵区域和
#
from sbw import *
# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        R,C=len(mat),len(mat[0])
        presums=[[0]*(C+1) for _ in range(R+1)]
        for i in range(R):
            for j in range(C):
                presums[i+1][j+1]=presums[i][j+1]+presums[i+1][j]+mat[i][j]-presums[i][j]
        ret=[[0]*C for _ in range(R)]
        for i in range(R):
            top=max(0,i-k)
            bottom=min(R-1,i+k)
            for j in range(C):
                left=max(0,j-k)
                right=min(C-1,j+k)
                ret[i][j]=presums[bottom+1][right+1]-presums[bottom+1][left]-presums[top][right+1]+presums[top][left]
        return ret
# @lc code=end
assert Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1)==[[12,21,16],[27,45,33],[24,39,28]]
