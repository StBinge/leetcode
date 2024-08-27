#
# @lc app=leetcode.cn id=807 lang=python3
# @lcpr version=30204
#
# [807] 保持城市天际线
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        N=len(grid)
        max_rows = [0] * N
        max_cols = [0] * N
        for r in range(N):
            for c in range(N):
                max_rows[r] = max(max_rows[r], grid[r][c])
                max_cols[c] = max(max_cols[c], grid[r][c])
        return sum(
            min(max_rows[r], max_cols[c]) - grid[r][c]
            for r in range(N)
            for c in range(N)
        )


# @lc code=end
assert Solution().maxIncreaseKeepingSkyline([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == 0
assert (
    Solution().maxIncreaseKeepingSkyline(
        [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    )
    == 35
)


#
# @lcpr case=start
# [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0,0],[0,0,0],[0,0,0]]\n
# @lcpr case=end

#
