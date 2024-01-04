#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
from sbw import *
# @lc code=start
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        q=[]
        for r in range(R):
            if grid[r][0]==1:
                q.append([r,0])
                grid[r][0]=0
            if grid[r][C-1]==1:            
                q.append([r,C-1])
                grid[r][C-1]=0
        for c in range(C):
            if grid[0][c]==1:
                q.append([0,c])
                grid[0][c]=0
            if grid[R-1][c]==1:            
                q.append([R-1,c])
                grid[R-1][c]=0  
        while q:
            r,c=q.pop()
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C and grid[nr][nc]==1:
                    grid[nr][nc]=0
                    q.append([nr,nc])
        
        return sum(sum(row) for row in grid)
        

# @lc code=end
grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
assert Solution().numEnclaves(grid)==0
grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
assert Solution().numEnclaves(grid)==3
