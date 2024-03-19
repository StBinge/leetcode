#
# @lc app=leetcode.cn id=1380 lang=python3
#
# [1380] 矩阵中的幸运数
#
from sbw import *
# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_max,k=0,0
        for row in matrix:
            ma=min(row)
            if ma>row_max:
                row_max=ma
                k=row.index(ma)
        return [row_max] if all(row[k]<=row_max for row in matrix) else []
# @lc code=end

