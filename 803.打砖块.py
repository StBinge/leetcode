#
# @lc app=leetcode.cn id=803 lang=python3
#
# [803] 打砖块
#
from typing import List
# @lc code=start
class Union:
    def __init__(self,n) -> None:
        self.p=list(range(n))
        self.sz=[1]*n
    
    def find(self,x):
        if x!=self.p[x]:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def merge(self,x,y):
        px,py=self.find(x),self.find(y)
        if px==py:
            return
        self.p[py]=px
        self.sz[px]+=self.sz[py]
    
    def size(self,x):
        return self.sz[self.find(x)]
    
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        R,C=len(grid),len(grid[0])
        def index(r,c):
            return r*C+c
        
        status=[row.copy() for row in grid]
        for r,c in hits:
            status[r][c]=0
        
        union=Union(R*C+1)

        root=R*C
        for r in range(R):
            for c in range(C):
                if status[r][c]==0:
                    continue
                idx=index(r,c)
                if r==0:
                    union.merge(c,root)
                if r>0 and status[r-1][c]:
                    union.merge(idx,index(r-1,c))
                if c>0 and status[r][c-1]:
                    union.merge(idx,index(r,c-1))
        
        dirs=[-1,0,1,0,-1]
        ret=[0]*len(hits)
        for i in range(len(hits)-1,-1,-1):
            r,c=hits[i]
            if grid[r][c]==0:
                continue
            idx=index(r,c)
            prev=union.size(root)
            if r==0:
                union.merge(idx,root)
            for d in range(4):
                nr,nc=r+dirs[d],c+dirs[d+1]
                if nr<0 or nr==R or nc<0 or nc==C or status[nr][nc]==0:
                    continue
                union.merge(idx,index(nr,nc))
            cur=union.size(root)
            ret[i]=max(0,cur-prev-1)
            status[r][c]=1
        return ret
# @lc code=end
grid=[[1],[1],[1],[1],[1]]
hits=[[3,0],[4,0],[1,0],[2,0],[0,0]]
assert Solution().hitBricks(grid,hits)==[1,0,1,0,0]

grid = [[1,0,0,0],[1,1,0,0]]
hits = [[1,1],[1,0]]
assert Solution().hitBricks(grid,hits)==[0,0]

grid = [[1,0,0,0],[1,1,1,0]]
hits = [[1,0]]
assert Solution().hitBricks(grid,hits)==[2]