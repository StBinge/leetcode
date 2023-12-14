#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
from sbw import *
# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N=len(grid)
        edges=deque()
        def find_edge(r,c):
            nonlocal N
            grid[r][c]=-1
            dirs=[-1,0,1,0,-1]
            cnt=0
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if nr<0 or nr==N or nc<0 or nc==N or grid[nr][nc]!=1:
                    continue
                find_edge(nr,nc)
                cnt+=1
            if cnt<4:
                edges.append((r,c,0))
        for r in range(N):
            for c in range(N):
                if grid[r][c]==1:
                    find_edge(r,c)
                    break
            if len(edges):
                break
        while True:
            r,c,dis = edges.popleft()
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<N and 0<=nc<N:
                    if grid[nr][nc]==1:
                        return dis
                    if grid[nr][nc]==0:
                        grid[nr][nc]=-1
                        edges.append([nr,nc,dis+1])
# @lc code=end
grid=[[0,1,0,0,0],[0,1,0,1,1],[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0]]
assert Solution().shortestBridge(grid)==1

grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
assert Solution().shortestBridge(grid)==1


grid = [[0,1,0],[0,0,0],[0,0,1]]
assert Solution().shortestBridge(grid)==2

grid = [[0,1],[1,0]]
assert Solution().shortestBridge(grid)==1
