#
# @lc app=leetcode.cn id=1210 lang=python3
#
# [1210] 穿过迷宫的最少移动次数
#
from sbw import *
# @lc code=start
class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        N=len(grid)
        Max=float('inf')
        f=[[[Max]*2 for _ in range(N)] for _ in range(N)]
        f[0][0][0]=0
        for i in range(N):
            for j in range(N):
                if grid[i][j]==1:
                    continue
                can_hori=j+1<N and grid[i][j+1]==0
                can_vert=i+1<N and grid[i+1][j]==0

                if can_hori:
                    if i>0:
                        f[i][j][0]=min(f[i][j][0],f[i-1][j][0]+1)
                    if j>0:
                        f[i][j][0]=min(f[i][j][0],f[i][j-1][0]+1)
                if can_vert:
                    if i>0:
                        f[i][j][1]=min(f[i][j][1],f[i-1][j][1]+1)
                    if j>0:
                        f[i][j][1]=min(f[i][j][1],f[i][j-1][1]+1)
                
                if can_hori and can_vert and grid[i+1][j+1]==0:
                    f[i][j][0]=min(f[i][j][0],f[i][j][1]+1)
                    f[i][j][1]=min(f[i][j][1],f[i][j][0]+1)
        return -1 if f[N-1][N-2][0]==Max else f[N-1][N-2][0]
# @lc code=end
grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
assert Solution().minimumMoves(grid)==11
