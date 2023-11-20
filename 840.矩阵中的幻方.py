#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
from typing import List


# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if R < 3 or C < 3:
            return 0
        ret = 0
        graph=[8,1,6,7,2,9,4,3]*2
        dr=[-1,-1,-1,0,1,1,1,0]
        dc=[-1,0,1,1,1,0,-1,-1]
        for r in range(1,R-1):
            for c in range(1,C-1):
                if grid[r][c]!=5:
                    continue
                around=[]
                for i in range(8):
                    around.append(grid[r+dr[i]][c+dc[i]])
                for i in range(8):
                    if graph[i]==around[0]:
                        if  around==graph[i:i+8] or around==graph[i+8:i:-1]:
                            ret+=1
        return ret


# @lc code=end
grid=[[8,3,4],[1,5,9],[6,7,2]]
assert Solution().numMagicSquaresInside(grid) == 1

grid = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]
assert Solution().numMagicSquaresInside(grid) == 1
