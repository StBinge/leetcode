#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
from typing import List
# @lc code=start
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        tag=[[-1]*n for _ in range(n)]
        areas={}

        idx=0
        
        def dfs(r,c):
            nonlocal idx,n
            tag[r][c]=idx
            areas[idx]=areas.get(idx,0)+1
            dirs=[-1,0,1,0,-1]
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if nr<0 or nr==n or nc<0 or nc==n or grid[nr][nc]==0 or tag[nr][nc]!=-1:
                    continue
                dfs(nr,nc)

        for r in range(n):
            for c in range(n):
                if grid[r][c] and tag[r][c]==-1:
                    dfs(r,c)
                    idx+=1
        
        ret=max(areas.values(),default=0)
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    continue
                counted=set()
                cnt=1
                dirs=[-1,0,1,0,-1]
                for i in range(4):
                    nr,nc=r+dirs[i],c+dirs[i+1]
                    if nr<0 or nr==n or nc<0 or nc==n or grid[nr][nc]==0:
                        continue
                    t=tag[nr][nc]
                    if t in counted:
                        continue
                    cnt+=areas[t]
                    counted.add(t)
                ret=max(ret,cnt)
        return ret
# @lc code=end
grid = [[1, 1], [1, 1]]
ret= 4
assert Solution().largestIsland(grid)==ret

grid = [[1, 1], [1, 0]]
ret= 4
assert Solution().largestIsland(grid)==ret
grid = [[1, 0], [0, 1]]
ret=3
assert Solution().largestIsland(grid)==ret


