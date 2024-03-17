#
# @lc app=leetcode.cn id=1463 lang=python3
#
# [1463] 摘樱桃 II
#
from sbw import *
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        R,C=len(grid),len(grid[0])
        # f=[[[float('-inf')] * (C+2) for _ in range(C+2)] for _ in range(R)]
        f0=[[float('-inf')] * (C+2) for _ in range(C+2)]
        f1=[[float('-inf')] * (C+2) for _ in range(C+2)]
        f0[1][-2]=grid[0][0]+grid[0][-1]
        for r in range(1,R):
            for i in range(C):
                for j in range(C):
                    cur=grid[r][i]+grid[r][j]
                    if i==j:
                        cur-=grid[r][i]
                    ma=float('-inf')
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            ma=max(ma,f0[i+1+di][j+1+dj])
                    f1[i+1][j+1]=ma+cur
            f0,f1=f1,f0
        return max(map(max,f0))
# @lc code=end
assert Solution().cherryPickup([[1,1],[1,1]])==4
assert Solution().cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]])==22
assert Solution().cherryPickup( [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])==28
assert Solution().cherryPickup([[3,1,1],[2,5,1],[1,5,5],[2,1,1]])==24
