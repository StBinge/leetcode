#
# @lc app=leetcode.cn id=2684 lang=python3
# @lcpr version=30204
#
# [2684] 矩阵中移动的最大次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        def dfs(r,c):
            if c==C-1:
                return C-1
            ret=c
            if r>0 and grid[r][c]<grid[r-1][c+1]:
                ret=max(ret,dfs(r-1,c+1))
            if grid[r][c]<grid[r][c+1]:
                ret=max(ret,dfs(r,c+1))
            if r+1<R and grid[r][c]<grid[r+1][c+1]:
                ret=max(ret,dfs(r+1,c+1))
            grid[r][c]=0
            return ret

        ret=0
        for r in range(R):
            ret=max(ret,dfs(r,0))
        return ret
# @lc code=end



#
# @lcpr case=start
# [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,2,4],[2,1,9],[1,1,7]]\n
# @lcpr case=end

#

