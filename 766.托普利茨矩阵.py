#
# @lc app=leetcode.cn id=766 lang=python3
#
# [766] 托普利茨矩阵
#
from typing import List
# @lc code=start
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        R,C=len(matrix),len(matrix[0])
        for r in range(1,R):
            for c in range(1,C):
                if matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True
# @lc code=end
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
assert Solution().isToeplitzMatrix(matrix)
matrix = [[1,2],[2,2]]
assert Solution().isToeplitzMatrix(matrix)==False
