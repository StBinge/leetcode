#
# @lc app=leetcode.cn id=3033 lang=python3
#
# [3033] 修改矩阵
#
from sbw import *
# @lc code=start
class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C=len(matrix),len(matrix[0])
        ret=[[0]*C for _ in range(R)]
        cols=[-1]*C
        def get_max(col):
            if cols[col]==-1:
                for i in range(R):
                    cols[col]=max(cols[col],matrix[i][col])
            return cols[col]
        for r in range(R):
            for c in range(C):
                if matrix[r][c]!=-1:
                    ret[r][c]=matrix[r][c]
                else:
                    ret[r][c]=get_max(c)
        return ret
# @lc code=end
assert Solution().modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]])==[[1,2,9],[4,8,6],[7,8,9]]
