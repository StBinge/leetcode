#
# @lc app=leetcode.cn id=1263 lang=python3
#
# [1263] 推箱子
#
from sbw import *
# @lc code=start
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        R,C=len(grid),len(grid[0])
        sx=sy=bx=by=tx=ty=0
        for r in range(R):
            for c in range(C):
                if grid[r][c]=='S':
                    sx,sy=r,c
                    grid[r][c]='.'
                elif grid[r][c]=='B':
                    bx,by=r,c
                    grid[r][c]='.'
                elif grid[r][c]=='T':
                    tx,ty=r,c
                    grid[r][c]='.'

        q=deque([(sx,sy,bx,by,0)])
        # def hash(sx,sy,bx,by):
        #     return sx+sy*20+bx*400+by*8000
        memo={(sx,sy,bx,by)}
        dirs=[-1,0,1,0,-1]
        # ret=float('inf')
        while q:
            sx,sy,bx,by,step=q.popleft()
            if tx==bx and ty==by:
                return step
            for i in range(4):
                nx,ny=sx+dirs[i],sy+dirs[i+1]
                if 0<=nx<R and 0<=ny<C and grid[nx][ny]=='.' and (nx!=bx or ny!=by) and (nx,ny,bx,by) not in memo:
                    q.appendleft((nx,ny,bx,by,step))
                    memo.add((nx,ny,bx,by))


            dis=abs(sx-bx)+abs(sy-by)
            if dis==1:
                dx,dy=bx-sx,by-sy
                nx,ny=bx+dx,by+dy
                if 0<=nx<R and 0<=ny<C and grid[nx][ny]=='.' and (bx,by,nx,ny) not in memo:
                    q.append((bx,by,nx,ny,step+1))
                    memo.add((bx,by,nx,ny))

        return -1
            
# @lc code=end
assert Solution().minPushBox([[".",".","#",".",".",".",".",".",".","."],[".","#",".","#","B","#",".","#",".","."],[".","#",".",".",".",".",".",".","T","."],["#",".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".",".","#"],[".",".",".",".",".",".",".",".","#","."],[".",".",".","#",".",".","#","#",".","."],[".",".",".",".","#",".",".","#",".","."],[".","#",".","S",".",".",".",".",".","."],["#",".",".","#",".",".",".",".",".","#"]]
)==5
assert Solution().minPushBox(grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]])==5

assert Solution().minPushBox(grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]])==-1
assert Solution().minPushBox(grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]])==3