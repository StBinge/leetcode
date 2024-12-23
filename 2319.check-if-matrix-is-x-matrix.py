#
# @lc app=leetcode.cn id=2319 lang=python3
# @lcpr version=30204
#
# [2319] 判断矩阵是否是一个 X 矩阵
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        N=len(grid)
        for r in range(N):
            for c in range(N):
                if not ((r==c or r+c==N-1) == (grid[r][c]!=0)):
                    return False
        return True
# @lc code=end
assert Solution().checkXMatrix([[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]])


#
# @lcpr case=start
# [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,7,0],[0,3,1],[0,5,0]]\n
# @lcpr case=end

#

