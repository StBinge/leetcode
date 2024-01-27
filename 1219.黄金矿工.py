#
# @lc app=leetcode.cn id=1219 lang=python3
#
# [1219] 黄金矿工
#
from sbw import *
# @lc code=start
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        def dfs(r,c):
            # if grid[r][c]==0:
            #     return 0
            
            dirs=[-1,0,1,0,-1]
            cache=grid[r][c]
            grid[r][c]=0
            ret=0
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc <C and grid[nr][nc]!=0:
                    ret=max(ret,dfs(nr,nc))
            grid[r][c]=cache
            return ret+cache
        
        ret=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    ret=max(ret,dfs(r,c))
        return ret
# @lc code=end
assert Solution().getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]])==28
assert Solution().getMaximumGold([[0,6,0],[5,8,7],[0,9,0]])==24
