#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
from typing import List
# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        ret=0
        row_heights=[0]*R
        col_heights=[0]*C
        for r in range(R):
            for c in range(C):
                if grid[r][c]==0:
                    continue
                ret+=2
                dirs=[-1,0,1,0,-1]
                for i in range(4):
                    nr,nc=r+dirs[i],c+dirs[i+1]
                    if 0<=nr<R and 0<=nc<C:
                        ret+=max(0,grid[r][c]-grid[nr][nc])
                    else:
                        ret+=grid[r][c]
        return ret
# @lc code=end
grid = [[2,2,2],[2,1,2],[2,2,2]]
assert Solution().surfaceArea(grid)==46

grid = [[1,1,1],[1,0,1],[1,1,1]]
assert Solution().surfaceArea(grid)==32

grid = [[1,2],[3,4]]
assert Solution().surfaceArea(grid)==34
