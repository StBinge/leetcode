#
# @lc app=leetcode.cn id=3195 lang=python3
# @lcpr version=30204
#
# [3195] 包含所有 1 的最小矩形面积 I
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        top=0
        while sum(grid[top])==0:
            top+=1
        bottom=R-1
        while sum(grid[bottom])==0:
            bottom-=1
        
        left=0
        while sum(grid[r][left] for r in range(R))==0:
            left+=1
        right=C-1
        while sum(grid[r][right] for r in range(R))==0:
            right-=1
        
        return (right-left+1)*(bottom-top+1)
# @lc code=end



#
# @lcpr case=start
# [[0,1,0],[1,0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,0],[1,0]]\n
# @lcpr case=end

#

