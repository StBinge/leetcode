#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] 二进制矩阵中的最短路径
#
from sbw import *
# @lc code=start
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        if len(grid)==1:
            return 1
        N=len(grid)

        q=deque([[0,0]])
        Max=N*N
        dist=[[Max]*N for _ in range(N)]
        dist[0][0]=1
        while q:
            r,c =q.popleft()
            if r==N-1 and c==N-1:
                return dist[r][c]
            for x in range(-1,2):
                for y in range(-1,2):
                    if x==y==0:
                        continue
                    nr,nc=r+x,c+y
                    if 0<=nr<N and 0<=nc<N and grid[nr][nc]==0 and dist[nr][nc]>dist[r][c]+1:
                        dist[nr][nc]=dist[r][c]+1
                        q.append([nr,nc])
        return -1

# @lc code=end
grid=[[0,0,0],[1,0,0],[1,1,0]]
assert Solution().shortestPathBinaryMatrix(grid)==3

grid=[[0,0,0],[1,1,0],[1,1,1]]
assert Solution().shortestPathBinaryMatrix(grid)==-1

grid = [[1,0,0],[1,1,0],[1,1,0]]
assert Solution().shortestPathBinaryMatrix(grid)==-1

grid = [[0,0,0],[1,1,0],[1,1,0]]
assert Solution().shortestPathBinaryMatrix(grid)==4

grid = [[0,1],[1,0]]
assert Solution().shortestPathBinaryMatrix(grid)==2
