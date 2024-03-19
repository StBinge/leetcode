#
# @lc app=leetcode.cn id=1391 lang=python3
#
# [1391] 检查网格中是否存在有效路径
#
from sbw import *
# @lc code=start
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        R,C=len(grid),len(grid[0])
        p=list(range(R*C))

        def find(x):
            if x!=p[x]:
                p[x]=find(p[x])
            return p[x]

        def connect(x,y):
            px,py=find(x),find(y)
            if px==py:
                return
            p[px]=py

        patterns=[0,0b1010,0b0101,0b1100,0b0110,0b1001,0b0011]
        dirs=[
            [-1,0],
            [0,1],
            [1,0],
            [0,-1],
        ]
        for r in range(R):
            for c in range(C):
                pat=patterns[grid[r][c]]
                for i,[dx,dy] in enumerate(dirs):
                    if pat & (1<<i) ==0:
                        continue
                    nr,nc=r+dx,c+dy
                    if not (0<=nr<R and 0<=nc<C):
                        continue
                    n_pat=patterns[grid[nr][nc]]
                    if n_pat & (1<<(i+2)%4):
                        connect(r*C+c,nr*C+nc)
        return find(0)==find(R*C-1)

# @lc code=end
assert Solution().hasValidPath([[6,1,3],[4,1,5]])
assert Solution().hasValidPath([[1]])
assert Solution().hasValidPath([[4,1],[6,1]])
assert Solution().hasValidPath(grid = [[1,1,2],[1,2,1]])==False
assert Solution().hasValidPath(grid = [[1,2,1],[1,2,1]])==False
assert Solution().hasValidPath([[2,4,3],[6,5,2]])
