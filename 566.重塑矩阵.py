#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#
from typing import List
# @lc code=start
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        R=len(mat)
        C=len(mat[0])
        total=R*C
        if total!=r*c or R==r:
            return mat
        
        ret=[[0]*c for _ in range(r)]
        idx=0
        for idx in range(total):
            ret[idx//c][idx%c]=mat[idx//C][idx%C]
  
        return ret
# @lc code=end

mat = [[1,2],[3,4]]
r = 1
c = 4
assert Solution().matrixReshape(mat,r,c)==[[1,2,3,4]]

mat = [[1,2],[3,4]]
r = 2
c = 4
assert Solution().matrixReshape(mat,r,c)==[[1,2],[3,4]]
