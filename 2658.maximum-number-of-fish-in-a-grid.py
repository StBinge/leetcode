#
# @lc app=leetcode.cn id=2658 lang=python3
# @lcpr version=30204
#
# [2658] 网格图中鱼的最大数目
#

from sbw import *

# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def bfs(r, c):
            ret = grid[r][c]
            grid[r][c] = 0
            dirs = [-1, 0, 1, 0, -1]
            for i in range(4):
                nr, nc = r + dirs[i], c + dirs[i + 1]
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] > 0:
                    ret += bfs(nr, nc)
            return ret

        ret = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 0:
                    ret = max(ret, bfs(r, c))
        return ret


# @lc code=end


#
# @lcpr case=start
# [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]\n
# @lcpr case=end

#
