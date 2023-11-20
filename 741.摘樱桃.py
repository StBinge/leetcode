#
# @lc app=leetcode.cn id=741 lang=python3
#
# [741] 摘樱桃
#
from typing import List
# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        L=len(grid)
        # f=[[[float('-inf')]*L for _ in range(L)] for _ in range(2*L-1)]
        # f[0][0][0]=grid[0][0]
        f=[[float('-inf')]*L for _ in range(L)]
        f[0][0]=grid[0][0]
        for k in range(1,2*L+1):
            for r1 in range(min(L,k+1)-1,max(0,k-L+1)-1,-1):
                c1=k-r1
                if grid[r1][c1]<0:
                    f[r1]=[float('-inf')]*L
                    continue
                for r2 in range(min(L,k+1)-1,r1-1,-1):
                    c2=k-r2
                    if grid[r2][c2] <0:
                        f[r1][r2]=float('-inf')
                        continue
                    pre_max=f[r1][r2]
                    if r1>0:
                        pre_max=max(pre_max,f[r1-1][r2])
                    if r2>0:
                        pre_max=max(pre_max,f[r1][r2-1])
                    if r1>0 and r2>0:
                        pre_max=max(pre_max,f[r1-1][r2-1])
                        
                    f[r1][r2]=pre_max+grid[r1][c1]
                    if r1!=r2:
                        f[r1][r2]+=grid[r2][c2]
        return max(f[-1][-1],0)
# @lc code=end
grid = [[0,1,-1],[1,0,-1],[1,1,1]]
assert Solution().cherryPickup(grid)==5
grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
assert Solution().cherryPickup(grid)==0
