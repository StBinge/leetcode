#
# @lc app=leetcode.cn id=2428 lang=python3
# @lcpr version=30204
#
# [2428] 沙漏的最大总和
#


# @lcpr-template-start
from sbw import *


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ret = 0
        R, C = len(grid), len(grid[0])
        for r in range(R - 2):
            top = grid[r][0] + grid[r][1]
            bottom = grid[r + 2][0] + grid[r+2][1]
            for c in range(2, C):
                top += grid[r][c]
                bottom += grid[r + 2][c]
                s = top + bottom + grid[r + 1][c - 1]
                ret = max(ret, s)
                top -= grid[r][c - 2]
                bottom -= grid[r+2][c - 2]
        return ret


# @lc code=end
assert Solution().maxSum([[1,2,3],[4,5,6],[7,8,9]])==35

#
# @lcpr case=start
# [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

#
