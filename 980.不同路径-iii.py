#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] 不同路径 III
#
from sbw import *


# @lc code=start
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        start = None
        mask=0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    start = [r, c]
                elif grid[r][c] == 0:
                    mask|=1<<(r*C+c)
        # vis={tuple(start)}

        @lru_cache
        def dp(r,c,mask:int):

            dirs=[-1,0,1,0,-1]
            ret=0
            for i in range(4):
                nr,nc=r+dirs[i],c+dirs[i+1]
                if 0<=nr<R and 0<=nc<C:
                    if grid[nr][nc]==2:
                        if mask==0:
                            ret+=1
                        continue
                    bit=1<<(nr*C+nc)
                    if mask & bit:
                        ret+=dp(nr,nc,mask ^ bit)
            return ret
        return dp(*start,mask)


# @lc code=end
grid = [[0, 1], [2, 0]]
assert Solution().uniquePathsIII(grid) == 0

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
assert Solution().uniquePathsIII(grid) == 4

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
assert Solution().uniquePathsIII(grid) == 2
