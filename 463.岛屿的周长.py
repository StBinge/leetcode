#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
from typing import List
# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ret=0
        R,C=len(grid),len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    if r==0 or grid[r-1][c]==0:
                        ret+=1
                    if c==0 or grid[r][c-1]==0:
                        ret+=1
        return ret<<1
# @lc code=end
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
assert Solution().islandPerimeter(grid)==16
grid = [[1]]
assert Solution().islandPerimeter(grid)==4
grid = [[1,0]]
assert Solution().islandPerimeter(grid)==4
