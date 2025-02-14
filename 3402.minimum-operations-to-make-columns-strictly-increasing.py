#
# @lc app=leetcode.cn id=3402 lang=python3
# @lcpr version=30204
#
# [3402] 使每一列严格递增的最少操作次数
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        ret=0
        for c in range(C):
            pre=-1
            for r in range(R):
                if grid[r][c]<=pre:
                    ret+=pre+1-grid[r][c]
                    pre+=1
                else:
                    pre=grid[r][c]
        return ret

# @lc code=end



#
# @lcpr case=start
# [[3,2],[1,3],[3,4],[0,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[3,2,1],[2,1,0],[1,2,3]]\n
# @lcpr case=end

#

