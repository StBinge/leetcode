#
# @lc app=leetcode.cn id=1559 lang=python3
#
# [1559] 二维网格图中探测环
#
from sbw import *
# @lc code=start
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        R,C=len(grid),len(grid[0])
        p=list(range(R*C))
        sz=[1]*(R*C)
        def find(x):
            if p[x]!=x:
                p[x]=find(p[x])
            return p[x]
        
        def unite(x,y):
            px,py=find(x),find(y)
            if px!=py:
                if sz[px]>sz[py]:
                    px,py=py,px
                p[px]=py
                sz[py]+=sz[px]

                return True
            return False
        
        for r in range(R):
            for c in range(C):
                if r>0 and grid[r-1][c]==grid[r][c]:
                    if not unite(r*C+c,(r-1)*C+c):
                        return True
                if c>0 and grid[r][c-1]==grid[r][c]:
                    if not unite(r*C+c,r*C+c-1):
                        return True
        pp=[[None]*C for _ in range(R)]
        for i in range(R*C):
            r,c=i//C,i%C
            pr,pc=p[i]//C,p[i]%C
            pp[r][c]=[pr,pc]
        return False
# @lc code=end

assert Solution().containsCycle(grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]])==True
assert Solution().containsCycle([["a","b","b"],["b","z","b"],["b","b","a"]])==False
assert Solution().containsCycle([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])==True