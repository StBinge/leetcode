#
# @lc app=leetcode.cn id=1162 lang=python3
#
# [1162] 地图分析
#
from sbw import *
# @lc code=start
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        lands=[]
        for r in range(R):
            for c in range(C):
                if grid[r][c]==1:
                    lands.append([r,c])
                    # grid[r][c]=-1
        if len(lands)==0 or len(lands)==R*C:
            return -1
        step=0
        dirs=[-1,0,1,0,-1]
        while lands:
            temp=[]
            for r,c in lands:
                for i in range(4):
                    nr,nc=r+dirs[i],c+dirs[i+1]
                    if 0<=nr<R and 0<=nc<C and grid[nr][nc]==0:
                        grid[nr][nc]=1
                        temp.append([nr,nc])
            lands=temp
            step+=1
        return step-1
# @lc code=end
assert Solution().maxDistance([[1,0,0],[0,0,0],[0,0,0]])==4
assert Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])==2
