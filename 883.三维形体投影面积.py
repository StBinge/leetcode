#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#
from typing import List
# @lc code=start
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ret=0
        R,C=len(grid),len(grid[0])
        x_heights=[0]*C
        y_heights=[0]*R
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    ret+=1
                    x_heights[c]=max(x_heights[c],grid[r][c])
                    y_heights[r]=max(y_heights[r],grid[r][c])
        return ret+sum(x_heights)+sum(y_heights)

# @lc code=end
assert Solution().projectionArea([[1,2],[3,4]])==17
assert Solution().projectionArea([[2]])==5
assert Solution().projectionArea([[1,0],[0,2]])==8
