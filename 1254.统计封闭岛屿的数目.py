#
# @lc app=leetcode.cn id=1254 lang=python3
#
# [1254] 统计封闭岛屿的数目
#
from sbw import *
# @lc code=start
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        def flood(r,c):
            grid[r][c]=1
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]==0:
                    flood(nr,nc)
        
        for r in range(R):
            if grid[r][0]==0:
                flood(r,0)
            if grid[r][C-1]==0:
                flood(r,C-1)
        
        for c in range(C):
            if grid[0][c]==0:
                flood(0,c)
            if grid[R-1][c]==0:
                flood(R-1,c)

        ret=0
        for r in range(1,R-1):
            for c in range(1,C-1):
                if grid[r][c]==0:
                    ret+=1
                    flood(r,c)
        return ret
# @lc code=end
grid=[
    [0,0,1,1,0,1,0,0,1,0],
    [1,1,0,1,1,0,1,1,1,0],
    [1,0,1,1,1,0,0,1,1,0],
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,1,0,1,0,1],
    [1,1,1,0,1,1,0,1,1,0]]

assert Solution().closedIsland(grid)==5

grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
assert Solution().closedIsland(grid)==2
assert Solution().closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])==1
assert Solution().closedIsland(grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]])==1
assert Solution().closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])==2
