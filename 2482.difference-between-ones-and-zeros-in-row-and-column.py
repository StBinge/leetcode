#
# @lc app=leetcode.cn id=2482 lang=python3
# @lcpr version=30204
#
# [2482] 行和列中一和零的差值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R,C=len(grid),len(grid[0])
        rows=[0]*R
        cols=[0]*C
        for r in range(R):
            for c in range(C):
                rows[r]+=grid[r][c]
                cols[c]+=grid[r][c]
        for r in range(R):
            for c in range(C):
                grid[r][c]=2*rows[r]-C+2*cols[c]-R
        return grid
# @lc code=end
assert Solution().onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])==[[0,0,4],[0,0,4],[-2,-2,2]]


#
# @lcpr case=start
# [[0,1,1],[1,0,1],[0,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,1,1]]\n
# @lcpr case=end

#

