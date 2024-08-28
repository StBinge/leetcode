#
# @lc app=leetcode.cn id=1727 lang=python3
#
# [1727] 重新排列后的最大子矩阵
#
from sbw import *


# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ret = 0
        for r in range(m):
            temp = []
            for c in range(n):
                if matrix[r][c] == 1:
                    heights[c] += 1
                    temp.append(heights[c])
                else:
                    heights[c] = 0
            l = len(temp)
            for i, h in enumerate(sorted(temp)):
                ret = max(ret, (l - i) * h)
        return ret


# @lc code=end
assert Solution().largestSubmatrix([[0, 0], [0, 0]]) == 0
assert Solution().largestSubmatrix([[1, 1, 0], [1, 0, 1]]) == 2
assert Solution().largestSubmatrix([[0, 0, 1], [1, 1, 1], [1, 0, 1]]) == 4
assert Solution().largestSubmatrix([[1, 0, 1, 0, 1]]) == 3
