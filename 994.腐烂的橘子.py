#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
from sbw import *
# @lc code=start
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        bads=[]
        goods=set()
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    bads.append([r,c])
                elif grid[r][c]==1:
                    goods.add((r,c))
        time=0
        while bads and len(goods):
            temp=[]
            for r,c in bads:
                dirs=[-1,0,1,0,-1]
                for i in range(4):
                    nr,nc=r+dirs[i],c+dirs[i+1]
                    if (nr,nc) in goods:
                        temp.append([nr,nc])
                        goods.remove((nr,nc))
            bads=temp
            time+=1
        return time if len(goods)==0 else -1

# @lc code=end
assert Solution().orangesRotting([[0,2]])==0

grid = [[2,1,1],[0,1,1],[1,0,1]]
assert Solution().orangesRotting(grid)==-1

grid = [[2,1,1],[1,1,0],[0,1,1]]
assert Solution().orangesRotting(grid)==4
