#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
from typing import List
# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        def dfs(r,c):
            nonlocal R,C
            # if grid[r][c]==0:
            #     return 0
            grid[r][c]=0
            dirs=[-1,0,1,0,-1]
            ret=1
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]:
                    ret+=dfs(nr,nc)
            return ret
        ret=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    area=dfs(r,c)
                    ret=max(ret,area)
        return ret
# @lc code=end

assert Solution().maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])==6