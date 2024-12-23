#
# @lc app=leetcode.cn id=2639 lang=python3
# @lcpr version=30204
#
# [2639] 查询网格图中每一列的宽度
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        # r,c=len(grid),len(grid[0])
        # ret=[0]*c
        return [len(str(max(max(col),min(col)*-10))) for col in zip(*grid)]
# @lc code=end
assert Solution().findColumnWidth([[-15,1,3],[15,7,12],[5,6,-2]])==[3,1,2]
assert Solution().findColumnWidth([[1],[22],[333]])==[3]


#
# @lcpr case=start
# [[1],[22],[333]]\n
# @lcpr case=end

# @lcpr case=start
# [[-15,1,3],[15,7,12],[5,6,-2]]\n
# @lcpr case=end

#

