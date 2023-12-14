#
# @lc app=leetcode.cn id=931 lang=python3
#
# [931] 下降路径最小和
#
from sbw import *


# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        Max = float("inf")
        for i in range(1, N):
            for c in range(N):
                left = matrix[i - 1][c - 1] if c > 0 else Max
                right = matrix[i - 1][c + 1] if c + 1 < N else Max
                matrix[i][c] = min(left, right, matrix[i - 1][c]) + matrix[i][c]
        return min(matrix[-1])


# @lc code=end
matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
assert Solution().minFallingPathSum(matrix) == 13
matrix = [[-19, 57], [-40, -5]]
assert Solution().minFallingPathSum(matrix) == -59
