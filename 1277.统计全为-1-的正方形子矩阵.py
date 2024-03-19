#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#
from sbw import *
# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R,C=len(matrix),len(matrix[0])
        f=[[0]*C for _ in range(R)]
        ret=0
        for r in range(R):
            for c in range(C):
                if r==0 or c==0:
                    f[r][c]=matrix[r][c]
                elif matrix[r][c]==0:
                    f[r][c]=0
                else:
                    f[r][c]=min(f[r-1][c],f[r-1][c-1],f[r][c-1])+1
                ret+=f[r][c]
        return ret
# @lc code=end
assert Solution().countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
])==7
assert Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])==15
