#
# @lc app=leetcode.cn id=3417 lang=python3
# @lcpr version=30204
#
# [3417] 跳过交替单元格的之字形遍历
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        ret=[]
        R,C=len(grid),len(grid[0])
        idx=0
        for r in range(R):
            if r&1==0:
                start=0
                end=C
                dir=1
            else:
                start=C-1
                end=-1
                dir=-1
            for c in range(start,end,dir):
                if idx==0:
                    ret.append(grid[r][c])
                idx^=1
        return ret
# @lc code=end



#
# @lcpr case=start
# [[1,2],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,1],[2,1],[2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

#

