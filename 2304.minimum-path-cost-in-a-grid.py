#
# @lc app=leetcode.cn id=2304 lang=python3
# @lcpr version=30204
#
# [2304] 网格中的最小路径代价
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        for r in range(R-2,-1,-1):
            for c in range(C):
                grid[r][c]+=min(g+c for g,c in zip(grid[r+1],moveCost[grid[r][c]]))
        return min(grid[0])
# @lc code=end
assert Solution().minPathCost(grid = [[5,1,2],[4,0,3]], moveCost = [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]])==6
assert Solution().minPathCost(grid = [[5,3],[4,0],[2,1]], moveCost = [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])==17


#
# @lcpr case=start
# [[5,3],[4,0],[2,1]]\n[[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,2],[4,0,3]]\n[[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]]\n
# @lcpr case=end

#

