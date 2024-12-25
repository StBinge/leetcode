#
# @lc app=leetcode.cn id=3142 lang=python3
# @lcpr version=30204
#
# [3142] 判断矩阵是否满足条件
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        R,C=len(grid),len(grid[0])
        for r in range(R-1):
            for c in range(C-1):
                if grid[r][c]!=grid[r+1][c] or grid[r][c]==grid[r][c+1]:
                    return False
        
        for r in range(R-1):
            if grid[r][-1]!=grid[r+1][-1]:
                return False
        
        for c in range(C-1):
            if grid[-1][c]==grid[-1][c+1]:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# [[1,0,2],[1,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1],[2],[3]]\n
# @lcpr case=end

#

