#
# @lc app=leetcode.cn id=959 lang=python3
#
# [959] 由斜杠划分区域
#
from sbw import *
# @lc code=start
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        # / =>1,2
        # \ =>3,4
        N=len(grid)
        size=N*N*4
        p=list(range(size))
        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]
        
        def connect(x,y):
            x,y=find(x),find(y)
            if x==y:
                return
            p[x]=y
        
        for i in range(N):
            for j in range(N):
                idx=i*N+j
                l=idx*4
                t=idx*4+1
                r=idx*4+2
                b=idx*4+3
                if grid[i][j]=='/':
                    connect(l,t)
                    connect(r,b)
                elif grid[i][j]==' ':
                    connect(l,t)
                    connect(l,r)
                    connect(l,b)
                else:
                    connect(l,b)
                    connect(r,t)
                if j+1<N:
                    right_l=(idx+1)*4
                    connect(r,right_l)
                if i+1<N:
                    bottom_t=(idx+N)*4+1
                    connect(b,bottom_t)
        return sum(i==n for i,n in enumerate(p))





# @lc code=end
grid = ["/\\","\\/"]
assert Solution().regionsBySlashes(grid)==5

grid = [" /","  "]
assert Solution().regionsBySlashes(grid)==1

grid = [" /","/ "]
assert Solution().regionsBySlashes(grid)==2
