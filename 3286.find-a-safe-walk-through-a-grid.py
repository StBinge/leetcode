#
# @lc app=leetcode.cn id=3286 lang=python3
# @lcpr version=30204
#
# [3286] 穿越网格图的安全路径
#


# @lcpr-template-start
from sbw import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R,C=len(grid),len(grid[0])
        total=R*C
        q=[]
        cache=[0]*total
        health-=grid[0][0]
        q=[[0,0,health]]
        cache[0]=health
        while q:
            x,y,h=q.pop()
            if h==0:
                continue
            if x==R-1 and y==C-1:
                return True
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nx=x+dirs[i]
                ny=y+dirs[i+1]
                if 0<=nx<R and 0<=ny<C:
                    _h=h-grid[nx][ny]
                    hash=nx*C+ny
                    if cache[hash]<_h:
                        cache[hash]=_h
                        q.append([nx,ny,_h])
        return False
# @lc code=end
assert Solution().findSafeWalk(grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5)
assert Solution().findSafeWalk(grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3)==False
assert Solution().findSafeWalk(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1)


#
# @lcpr case=start
# [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]\n1\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n5\n
# @lcpr case=end

#

