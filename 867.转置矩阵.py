#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#
from typing import List
# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R,C=len(matrix),len(matrix[0])
        ret=[[0]*R for _ in range(C)]
        for r in range(R):
            for c in range(C):
                ret[c][r]=matrix[r][c]
        return ret
# @lc code=end

